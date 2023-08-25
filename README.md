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

## Considerations and Assumptions
Per the BibJSON spec, the default set of keys are based off of the bibtex spec. My transformer currently only utilizes the apparent keys in each entry of the provided sample. 
Each sample generally has the same core keys and many of the default bibtex keys are missing. Making my transformer to adhere to these missing keys would be a set of minor changes.
The provided sample file is quite small, so regarding memory usage it isn't too bad, but if the transformer is used with a very large file, the potential memory usage could be a source of issues.

