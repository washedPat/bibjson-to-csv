import argparse
import json
import csv

HEADER = ["_xddid", "doi", "_gddid", "title", "type", "journal", "link_type", "link", "author", "publisher", "volume", "pages", "year"]

def bibjson_entry_to_row(entry, filler):
    row = []
    
    xddid = filler 
    doi = filler
    for ids in entry.get("identifier", []):
            if ids["type"] == "doi":
                doi = ids["id"]
            if ids["type"] == "_xddid":
                xddid = ids["id"]

    gddid = entry.get("_gddid", filler)
    title = entry.get("title", filler)
    entry_type = entry.get("type", filler)
    journal = entry.get("journal", {}).get("name", filler)
    link = entry.get("link", [{}])[0].get("url", filler)
    link_type = entry.get("link", [{}])[0].get("type", filler)
    author = '; '.join([item['name'] for item in entry.get('author', [])])
    publisher = entry.get("publisher", filler)
    volume = entry.get("volume", filler)
    pages = entry.get("pages", filler)
    year = entry.get("year", filler)    

    row = [xddid, doi, gddid, title, entry_type, journal, link_type, link, author, publisher, volume, pages, year]

    return row

def bibJSONtoCSV(in_file, out_file, filler):
    bibjson_data = json.load(in_file) 

    with out_file as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        
        for entry in bibjson_data:
            row = bibjson_entry_to_row(entry, filler)
            writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--infile", help="BibJSON file path", type=argparse.FileType('r'), required=True)
    parser.add_argument("-o", "--outfile", help="output file path", type=argparse.FileType('w'), required=True)
    parser.add_argument("-f", "--missing-column-filler", 
                        help="value that should be used as the filler for missing values in a column. the default is just an empty string", 
                        type=str, default="", required=False)

    args = parser.parse_args()

    bibJSONtoCSV(args.infile, args.outfile, args.missing_column_filler)
