# BibJSON To CSV - Data Engineer - Programming Test
This is a data conversion tool used to parse BibJSON files and transform them into CSV file.
I decided to use Python as it has great standard libraries for handling strings, parsing arguments, json and csv files.
The program is self contained in the `main.py` file. 

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
--full-spec true
```
Help
```shell
docker run \
-v $(pwd)/data:/usr/src/app/data \
bibjson-to-csv \
-h
```

## Considerations and Assumptions
Per the BibJSON spec, the default set of keys are based off of the bibtex spec. My transformer currently only utilizes the apparent keys in each entry of the provided sample. 
Each sample generally has the same core keys and many of the default bibtex keys are missing. Making my transformer to adhere to these missing keys would be a set of minor changes.
The provided sample file is quite small, so regarding memory usage it isn't too bad, but if the transformer is used with a very large file, the potential memory usage could be a source of issues.

