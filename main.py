import argparse
import json
import csv

SMALL_SPEC_HEADER = ["_xddid", "doi", "_gddid", "title", "type", "journal", "link_type", "link", "author", "publisher", "volume", "pages", "year"]
FULL_SPEC_HEADER = [
    "_xddid", "doi", "_gddid", "title", "type", "journal", "link_type", "link",
    "author", "publisher", "volume", "pages", "year", "address", "annote",
    "booktitle", "email", "chapter", "crossref", "edition", "editor",
    "howpublished", "institution", "key", "month", "note", "number",
    "organization", "school", "series"
]

# common fields held between each sample provided by the sample bibjson file
# the filler argument is used to provide custom fillers
def common_entry_to_row(entry, filler):
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

def bibjson_entry_to_row(entry, filler):
    return common_entry_to_row(entry, filler)

# adds the full spec of fields to the common fields
def bibjson_entry_to_row_full(entry, filler):
    common_row = common_entry_to_row(entry, filler)

    # Additional fields in the full spec
    address = entry.get("address", filler)
    annote = entry.get("annote", filler)
    booktitle = entry.get("booktitle", filler)
    email = entry.get("email", filler)
    chapter = entry.get("chapter", filler)
    crossref = entry.get("crossref", filler)
    edition = entry.get("edition", filler)
    editor = entry.get("editor", filler)
    howpublished = entry.get("howpublished", filler)
    institution = entry.get("institution", filler)
    key = entry.get("key", filler)
    month = entry.get("month", filler)
    note = entry.get("note", filler)
    number = entry.get("number", filler)
    organization = entry.get("organization", filler)
    school = entry.get("school", filler)
    series = entry.get("series", filler)

    full_row = common_row + [address, annote, booktitle, email, chapter, crossref, edition, editor,
                             howpublished, institution, key, month, note, number, organization, school, series]

    return full_row

# transformer logic
# 1. parse bibjson file
# 2. open csv file
# 3. write the appropriate header
# 4. write the appropriate rows for each entry with the optional filler value for missing values
def bibJSONtoCSV(in_file, out_file, filler="", full_spec=False):
    bibjson_data = json.load(in_file) 

    def write_rows(writer, row_func):
        for entry in bibjson_data:
            row = row_func(entry, filler)
            writer.writerow(row)

    with out_file as f:
        writer = csv.writer(f)
        if not full_spec:
            writer.writerow(SMALL_SPEC_HEADER)
            write_rows(writer, bibjson_entry_to_row)
        else:
            writer.writerow(FULL_SPEC_HEADER)
            write_rows(writer, bibjson_entry_to_row_full)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--infile", help="BibJSON file path", type=argparse.FileType('r'), required=True)
    parser.add_argument("-o", "--outfile", help="output file path", type=argparse.FileType('w'), required=True)
    parser.add_argument("-f", "--missing-column-filler", 
                        help="value that should be used as the filler for missing values in a column. the default is just an empty string", 
                        type=str, default="", required=False)
    parser.add_argument("--full-spec", help="Use the full spec of the bibtex/bibjson", action="store_true", required=False)

    args = parser.parse_args()

    bibJSONtoCSV(args.infile, args.outfile, args.missing_column_filler, args.full_spec)
