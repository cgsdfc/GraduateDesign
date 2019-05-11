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


K_BOOKTITLE = 'booktitle'
K_ID = 'ID'


class BibMaker:
    IGNORED_DIR = 'other'

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

    # Keys we *don't* need.
    BACK_LIST = {
        'crossref',
        'url',
        'timestamp',
        'biburl',
        'bibsource',
        'eprint',
        'archiveprefix',
    }

    def __init__(self, stop_at_empty=False, white_list_only=True):
        self.stop_at_empty = stop_at_empty
        self.white_list_only = white_list_only

    def count_matched_keys(self, bib: dict):
        """
        Count the matched keys of bib against the white list.
        :param bib:
        :return:
        """
        # The current criteria for selecting is the number of matches of keys in the white list.
        return bib, len(list(filter(lambda k: k in self.WHITE_LIST, bib.keys())))

    def extract_bib_entry(self, filename):
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
                return None

        entry, n_matched = max([self.count_matched_keys(bib) for bib in bib_db.entries], key=operator.itemgetter(1))
        logging.info('extract %s from %s', entry[K_ID], filename)
        return entry

    def make_bibs(self, prefix, output):
        all_bibs = self.find_all_bibs(prefix)
        all_bibs = [self.cleanup(bib) for bib in all_bibs]

        bib_db = BibDatabase()
        bib_db.entries = all_bibs
        writer = BibTexWriter()
        writer.indent = '\t'

        with open(output, 'w') as f:
            bibtexparser.dump(bib_db, f, writer)
        logging.info('processed %d bib entries', len(all_bibs))

    def find_all_files(self, src_dir):
        files = pathlib.Path(src_dir).rglob('*.bib')
        # put things into other/ and ignore them.
        files = filter(lambda p: self.IGNORED_DIR not in p.parent.parts, files)
        return list(files)

    def find_all_bibs(self, src_dir):
        files = self.find_all_files(src_dir)
        bib_keys = set()
        bib_list = []

        for file in files:
            bib = self.extract_bib_entry(file)
            if bib is None:
                if self.stop_at_empty:
                    raise EmptyBibFile(file)
                logging.warning('empty bib file: {}'.format(file))
            else:
                if bib[K_ID] in bib_keys:
                    logging.warning('duplicate bib entry: %s from %s', bib[K_ID], file)
                    continue
                bib_keys.add(bib[K_ID])
                bib_list.append(bib)

        return bib_list

    def remove_black_list_keys(self, bib: dict):
        for key in self.BACK_LIST:
            if key in bib:
                del bib[key]
        return bib

    def remove_keys_not_in_white_list(self, bib: dict):
        excluded_keys = [key for key in bib.keys() if key.islower() and key not in self.WHITE_LIST]
        for key in excluded_keys:
            del bib[key]

    def normalize_values(self, bib: dict):
        if K_BOOKTITLE in bib:
            value = bib[K_BOOKTITLE]
            value = value.split(',')[0]
            bib[K_BOOKTITLE] = value
        return bib

    def cleanup(self, bib: dict):
        bib = self.remove_black_list_keys(bib)
        bib = self.normalize_values(bib)
        if self.white_list_only:
            self.remove_keys_not_in_white_list(bib)
        return bib


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prefix', help='root to the bib database')
    parser.add_argument('-o', '--output', help='output file of the merged and cleaned single file')
    parser.add_argument('-white-list-only', action='store_true', help='only keep those keys in the white list')
    parser.add_argument('-stop-at-empty', action='store_true', help='stop when an empty bib file was found')
    args = parser.parse_args()

    maker = BibMaker(
        stop_at_empty=args.stop_at_empty,
        white_list_only=args.white_list_only,
    )
    maker.make_bibs(
        prefix=args.prefix,
        output=args.output,
    )
