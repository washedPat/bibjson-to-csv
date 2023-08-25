# BibJSON To CSV - Data Engineer - Programming Test
This is a data conversion tool used to parse BibJSON files and transform them into CSV file.
I decided to use Python as it has great standard libraries for handling strings, parsing arguments, json and csv files.
The program is self contained in the `main.py` file. 

## Usage
With default filler
```shell
python main.py -i data/xdd_sample.bibjson -o data/xdd_sample.csv
```
With custom filler
```shell
python main.py -i data/xdd_sample.bibjson -o data/xdd_sample.csv -f n/a
```
Help
```
python main.py -h
```
