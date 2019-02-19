# SSW 555 Project

![](https://img.shields.io/badge/Language-Python-brightgreen.svg) ![](https://img.shields.io/badge/Release-V1.1-blue.svg) ![](https://img.shields.io/badge/License-MIT-orange.svg)


## Introduction

This is a project for SSW-555 (Agile Methods for Software Development). This application is a command line program written in Python which takes in GEDCOM files, parses them, then stores and returns the data in neat tables.

## Repo Organization 

```bash 
├── README.md
├── TeamXXReport.xlsx
├── __pycache__
│   ├── readGed.cpython-36.pyc
│   ├── readGed.cpython-37.pyc
│   ├── unit32test.cpython-36.pyc
│   ├── unit32test.cpython-37.pyc
│   ├── unit_test.cpython-36.pyc
│   ├── unit_test.cpython-37.pyc
│   ├── us03.cpython-36.pyc
│   ├── us03_test.cpython-36.pyc
│   ├── us16.cpython-36.pyc
│   ├── us16.cpython-37.pyc
│   ├── us29.cpython-36.pyc
│   ├── us29.cpython-37.pyc
│   ├── us32.cpython-36.pyc
│   └── us32.cpython-37.pyc
├── input.ged
├── inputGed5.ged
├── input_1.ged
├── input_2.ged
├── input_3.ged
├── input_4.ged
├── output.txt
├── readGed.py
├── unit_test.py
├── us02.py
├── us03.py
├── us16.py
├── us29.py
└── us32.py
```

Proposed Organization 

```bash 
├── README.md
├── TeamXXReport.xlsx
├── data
│   ├── input.ged
│   ├── input_1.ged
│   ├── input_2.ged
│   ├── input_3.ged
│   ├── input_4.ged
│   ├── input_5.ged
├── readGed.py
├── results 
│   ├── output.txt
├── unit_test.py
├── userStories 
│   ├── us02.py
│   ├── us03.py
│   ├── us16.py
│   ├── us29.py
│   ├── us32.py
```

## Authors

[Rakshak Kumar](https://github.com/rakshak10)
[Chloe Quinto](https://github.com/chloequinto)
[Mengyuan Wang](https://github.com/stdlibrainbow)
[Matthew Wisnewski](https://github.com/mwisnews)
[Renjie Zhou](https://github.com/rzhou10)

## Running and Installation
1. Clone or download the repo
2. Run readGed.py
3. Check results > output.txt for results 