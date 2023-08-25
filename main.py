import argparse
import json
import csv

def bibJSONtoCSV(in_file, out_file):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--infile", help="BibJSON file path", type=argparse.FileType('r'), required=True)
    parser.add_argument("-o", "--outfile", help="output file path", type=argparse.FileType('w'), required=True)

    args = parser.parse_args()

    bibJSONtoCSV(args.infile, args.outfile)
