import bibtexparser
import argparse
from pprint import pprint


def get_white_list(bib_file):
    with open(bib_file) as f:
        db = bibtexparser.load(f)
    entries = db.entries

    def extract_keys(entries):
        for bib in entries:
            for key in bib.keys():
                if key.islower():
                    yield key

    return set(extract_keys(entries))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='reference bib file')
    args = parser.parse_args()
    white_list = get_white_list(args.input)
    pprint(white_list)
