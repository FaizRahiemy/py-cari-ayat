from flask import render_template, request

from py_cari_ayat.ayat import router_ayat, cosine_similarity
from py_cari_ayat.models.kata import Kata

@router_ayat.route('/query/<query_str>') 
def query(query_str: str):
    query_katas: list[Kata] = [Kata(query) for query in query_str.split()]
    results: list[Kata] = cosine_similarity.get_similar(query_str)
    return render_template(
        'ayat/query.html.j2',
        request=request,
        title="Cari Ayat",
        description="Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.",
        query_katas=query_katas,
        results=results
    )