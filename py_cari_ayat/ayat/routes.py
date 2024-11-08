from flask import render_template, request

from py_cari_ayat.ayat import router_ayat

@router_ayat.route('/query/<query_str>') 
def query(query_str: str):
    return render_template(
        'ayat/query.html',
        request=request,
        title="Cari Ayat",
        description="Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.",
        query_str=query_str
    )

@router_ayat.route('/{id}') 
def ayat():
    return render_template(
        'surat/surat.html',
        request=request,
        title="Cari Ayat",
        description="Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity."
    )