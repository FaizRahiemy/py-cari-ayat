from flask import render_template, request

from py_cari_ayat.surat import router_surat
from py_cari_ayat.models.surat import Surat

@router_surat.route('/') 
def surats():
    surats: list[Surat] = Surat.query.all()
    print(f'len: {len(surats)}')
    return render_template(
        'surat/surats.html',
        request=request,
        title='Cari Ayat',
        description='Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.',
        surats = surats
    )