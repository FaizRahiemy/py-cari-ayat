from flask import render_template, request, redirect, url_for

from py_cari_ayat.ayat import router_ayat, cosine_similarity
from py_cari_ayat.models.ayat import Ayat
from py_cari_ayat.models.kata import Kata

@router_ayat.route('/query/<query_str>') 
def query(query_str: str):
    query_katas: list[Kata] = [Kata(query) for query in query_str.split()]
    results: list[Kata] = cosine_similarity.get_similar(query_str)
    return render_template(
        'ayat/query.html.j2',
        request=request,
        title=f'Cari Ayat - {query_str}',
        description='Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.',
        query_katas=query_katas,
        results=results
    )

@router_ayat.route('/<id>') 
def ayat(id: int):
    ayat: Ayat|None = Ayat.query.get(id)
    prev_ayat: int = int(id) - 1
    if int(id) == 1:
        prev_ayat = 1204
    next_ayat: int = int(id) + 1
    if int(id) == 1204:
        next_ayat = 1
    if ayat is None:
        return redirect(url_for('router_surat.surats', notfound=True))
    return render_template(
        'ayat/ayat.html.j2',
        request=request,
        title=f'Cari Ayat - QS:{ayat.surat_id}-{ayat.ayat}',
        description='Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.',
        ayat=ayat,
        prev_ayat=prev_ayat,
        next_ayat=next_ayat
    )