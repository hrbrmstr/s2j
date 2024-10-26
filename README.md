# s2j

A Python utility that reads in Suricata rules and outputs JSON.

## Installation

```bash
$ python3 -m pip install -e git+https://codeberg.org/hrbrmstr/s2j.git#egg=s2j
```

## Usage

```bash
s2j < rules.txt > rules.json
```

Or:

```bash
cat rules.txt | s2j > rules.json
```

Or:

```bash
s2j rules.txt > rules.json
```
