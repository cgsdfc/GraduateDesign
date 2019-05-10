import operator
import bibtexparser
import argparse
import logging
import pathlib

from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser


class EmptyBibFile(Exception):
    pass


IGNORE_SUBDIR = 'misc'

# Keys we *don't* need.
BACK_LIST = (
    'crossref',
    'url',
    'timestamp',
    'biburl',
    'bibsource',
    'eprint',
    'archiveprefix',
)

# Keys we need.
WHITE_LIST = {
    'author',
    'booktitle',
    'editor',
    'journal',
    'number',
    'pages',
    'publisher',
    'title',
    'volume',
    'year',
}

BOOKTITLE = 'booktitle'
ID = 'ID'


def get_bib_from_file(filename):
    """
    Extract the main bib dict from a bib files.
    Bib files downloaded from DBLP usually contains multiple entries for the same paper.

    :param filename: the file containing one or more bib entries.
    :return: dict the extracted bib.
    """
    parser = BibTexParser(common_strings=True)
    with open(filename) as f:
        try:
            bib_db: BibDatabase = bibtexparser.load(f, parser)
        except IndexError:
            raise EmptyBibFile(filename) from None

    def match_keys_against_white_list(bib: dict):
        """
        Count the matched keys of bib against the white list.
        :param bib:
        :return:
        """
        return bib, sum(1 for key in bib.keys() if key in WHITE_LIST)

    # The current criteria for selecting is the number of matches of keys in the white list.
    max_bib, max_matches = max([match_keys_against_white_list(bib) for bib in bib_db.entries],
                               key=operator.itemgetter(1))
    logging.info('extract %s from %s', max_bib[ID], filename)
    return max_bib


def get_all_bibs(prefix, stop_at_empty):
    def get_all_bib_files():
        bibs = pathlib.Path(prefix).rglob('*.bib')
        return bibs

    files = get_all_bib_files()
    bib_keys = set()
    bib_list = []

    for bib_file in files:
        try:
            bib = get_bib_from_file(bib_file)
        except EmptyBibFile as e:
            if stop_at_empty:
                raise
            logging.warning('empty bib file: %s', e.args[0])
        else:
            if not bib or bib[ID] in bib_keys:
                logging.warning('duplicate bib entry: %s from %s', bib[ID], bib_file)
                continue
            bib_keys.add(bib[ID])
            bib_list.append(bib)

    return bib_list


def remove_black_list_keys(bib: dict):
    for key in BACK_LIST:
        if key in bib:
            del bib[key]
    return bib


def remove_keys_not_in_white_list(bib: dict):
    excluded_keys = [key for key in bib.keys() if key.islower() and key not in WHITE_LIST]
    for key in excluded_keys:
        del bib[key]


def normalize_values(bib: dict):
    if BOOKTITLE in bib:
        value = bib[BOOKTITLE]
        value = value.split(',')[0]
        bib[BOOKTITLE] = value
    return bib


def cleanup(bib: dict, white_list_only: bool):
    bib = remove_black_list_keys(bib)
    bib = normalize_values(bib)
    if white_list_only:
        remove_keys_not_in_white_list(bib)
    return bib


def main(args):
    all_bibs = get_all_bibs(args.prefix, args.stop_at_empty)
    all_bibs = [cleanup(bib, args.white_list_only) for bib in all_bibs]
    bib_db = BibDatabase()
    bib_db.entries = all_bibs

    writer = BibTexWriter()
    writer.indent = '\t'
    with open(args.output, 'w') as f:
        bibtexparser.dump(bib_db, f, writer)
    logging.info('processed %d bib entries', len(all_bibs))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prefix', help='root to the bib database')
    parser.add_argument('-o', '--output', help='output file of the merged and cleaned single file')
    parser.add_argument('-white-list-only', action='store_true', help='only keep those keys in the white list')
    parser.add_argument('-stop-at-empty', action='store_true', help='stop when an empty bib file was found')
    args = parser.parse_args()
    main(args)
