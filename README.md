# Py Cari Ayat
Py Cari Ayat is a Python Flask version of the [original](https://github.com/FaizRahiemy/cari-ayat) Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity. Apart from porting the codes from PHP to Python Flask, this variant of Cari Ayat is also fixing cosine-similarity `xy` variable, where on the PHP version the `xy` (or in the legacy code, they are defined as `ayatKeyCampur`, `kataPecahCampur` & `ayatPecah`) keeps appending for all matched words (it should be reset once checking the next word). UI of the search engine is intended to use Indonesian as the search engine is optimized for Indonesian-spell query.

## Feature
* Verse search engine by using Indonesian spelling
* Quran Juz 1-6 & 30 database

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