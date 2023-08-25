import argparse
import json
import csv
import pprint

HEADER = ["_xddid", "doi", "_gddid", "title", "type", "journal", "link_type", "link", "author", "publisher", "volume", "pages", "year"]

def bibjson_entry_to_row(entry):
    row = []
    
    xddid = ""
    doi = ""
    try:
        for ids in entry["identifier"]:
            if ids["type"] == "doi":
                doi = ids["id"]
            if ids["type"] == "_xddid":
                xddid = ids["id"]
        
        gddid = entry["_gddid"]
        title = entry["title"]
        entry_type = entry["type"]
        journal = entry["journal"]["name"]
        link = entry["link"][0]["url"]
        link_type = entry["link"][0]["type"]
        author = '; '.join([item['name'] for item in entry['author']])
        publisher = entry["publisher"]
        volume = entry["volume"]
        pages = entry["pages"]
        year = entry["year"]
    except Exception as e:
        print(e)
        pprint.pprint(entry)
        exit(0)


    row = [xddid, doi, gddid, title, entry_type, journal, link_type, link, author, publisher, volume, pages, year]

    return row

def bibJSONtoCSV(in_file, out_file):
    bibjson_data = json.load(in_file) 

    with out_file as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        
        for entry in bibjson_data:
            row = bibjson_entry_to_row(entry)
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--infile", help="BibJSON file path", type=argparse.FileType('r'), required=True)
    parser.add_argument("-o", "--outfile", help="output file path", type=argparse.FileType('w'), required=True)

    args = parser.parse_args()

    bibJSONtoCSV(args.infile, args.outfile)
