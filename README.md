# Py Cari Ayat
Py Cari Ayat is a python flask version of the [original](https://github.com/FaizRahiemy/cari-ayat) Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.

## Feature
* Verse search engine by using Indonesian spelling
* Quran Juz 30 database

## Requirements
List of requirements:
* python = "^3.10"
* flask = "^3.0.3"
* sqlalchemy = "^2.0.35"
* gunicorn = "^23.0.0"
* flask-sqlalchemy = "^3.1.1"
* pyyaml = "^6.0.2"

Install with poetry:
```
poetry install
```

## How to Use?
Once you prepared the requierements:

### Set Environment Variable
Set `py_cari_ayat` as the environment variable:

Windows
```
$env:FLASK_APP="py_cari_ayat"
```
Unix - Linux/Mac
```
FLASK_APP="py_cari_ayat"
```

### Run
Below are the steps to run the app. Ensure you are already in the py-cari-ayat directory.

Vanilla Flask:
```
flask run
```
Poetry:
```
poetry run flask run
```