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


BACK_LIST = (
    'crossref',
    'url',
    'timestamp',
    'biburl',
    'bibsource',
    'eprint',
    'archiveprefix',
)

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


def get_all_bib_files(prefix):
    return pathlib.Path(prefix).rglob('*.bib')


def get_bib_from_file(filename, stop_at_empty: bool):
    parser = BibTexParser(common_strings=True)
    with open(filename) as f:
        try:
            bib_db: BibDatabase = bibtexparser.load(f, parser)
        except IndexError:
            if stop_at_empty:
                # suppress the ugly str index out of range.
                raise EmptyBibFile(filename) from None
            else:
                logging.warning('empty bib file: %s', filename)
                return {}

    def match_keys_against_white_list(bib: dict):
        return bib, sum(1 for key in bib.keys() if key in WHITE_LIST)

    max_bib, max_matches = max([match_keys_against_white_list(bib) for bib in bib_db.entries],
                               key=operator.itemgetter(1))
    logging.info('extract %s from %s', max_bib[ID], filename)
    return max_bib


def remove_black_list_keys(bib: dict):
    for key in BACK_LIST:
        if key in bib:
            del bib[key]
    return bib


def normalize_values(bib: dict):
    if BOOKTITLE in bib:
        value = bib[BOOKTITLE]
        logging.info('old: %s', value)
        value = value.split(',')[0]
        logging.info('new: %s', value)
        bib[BOOKTITLE] = value
    return bib


def cleanup(bib: dict, white_list_only: bool):
    bib = remove_black_list_keys(bib)
    bib = normalize_values(bib)

    if white_list_only:
        excluded_keys = [key for key in bib.keys() if key.islower() and key not in WHITE_LIST]
        for key in excluded_keys:
            del bib[key]
    return bib


def main(args):
    all_bibs = [get_bib_from_file(filename, args.stop_at_empty) for filename in get_all_bib_files(args.prefix)]
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
