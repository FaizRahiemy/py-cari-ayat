from flask import redirect, render_template, request, url_for

from py_cari_ayat.surat import router_surat
from py_cari_ayat.models.surat import Surat

@router_surat.route('/') 
def surats():
    surats: list[Surat] = Surat.query.all()
    return render_template(
        'surat/surats.html.j2',
        request=request,
        title='Cari Ayat',
        description='Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.',
        surats = surats
    )

@router_surat.route('/<id>') 
def surat(id: int):
    surat: Surat | None = Surat.query.get(id)
    if surat is None:
        return redirect(url_for('router_surat.surats', notfound=True))
    return render_template(
        'surat/surat.html.j2',
        request=request,
        title='Cari Ayat',
        description='Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.',
        surat = surat
    )