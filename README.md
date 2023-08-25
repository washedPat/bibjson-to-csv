# BibJSON To CSV - Data Engineer - Programming Test
This is a data conversion tool used to parse BibJSON files and transform them into CSV file.
I decided to use Python as it has a great set of standard libraries for handling strings, parsing arguments, json and csv files.
The program is self contained in the `main.py` file. 

## Considerations
When writing the transformer, I initially just supported the common keys within each entry of the BibJSON file. 
After further examination of the BibJSON specification, I found that the default set of keys is from the BibTeX specification.
The BibJSON specification is very loose and allows for missing values. As such I found it reasonable to enable the full specification via a feature flag.
By default the program fills missing values with nothing, leaving an empty value in row. However I added a flag to allow for custom fillers to suite the needs of the user.

## Requirements
Either:
- Python
- Docker

## Usage
You are able to run the parser either directly from Python or you can build and run the Docker container.

### Python

With default filler
```shell
python main.py -i data/xdd_sample.bibjson -o data/xdd_sample.csv
```
With custom filler
```shell
python main.py -i data/xdd_sample.bibjson -o data/xdd_sample.csv -f n/a
```
With the full BibTeX/BibJSON spec
```shell
python main.py -i data/xdd_sample.bibjson -o data/xdd_sample.csv --full-spec
```
Help
```
python main.py -h
```

### Docker
Build the container
```shell
docker build -t bibjson-to-csv .
```
Run the container with default missing value filler
```shell
docker run \
-v $(pwd)/data:/usr/src/app/data \
bibjson-to-csv \
-i /usr/src/app/data/xdd_sample.bibjson \
-o /usr/src/app/data/xdd_sample.csv
```
Run the container with custom missing value filler
```shell
docker run \
-v $(pwd)/data:/usr/src/app/data \
bibjson-to-csv \
-i /usr/src/app/data/xdd_sample.bibjson \
-o /usr/src/app/data/xdd_sample.csv \
-f n/a
```
Run the container with the full BibTeX/BibJSON spec
```shell
docker run \
-v $(pwd)/data:/usr/src/app/data \
bibjson-to-csv \
-i /usr/src/app/data/xdd_sample.bibjson \
-o /usr/src/app/data/xdd_sample.csv \
--full-spec
```
Help
```shell
docker run \
-v $(pwd)/data:/usr/src/app/data \
bibjson-to-csv \
-h
```
