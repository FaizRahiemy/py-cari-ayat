from flask import render_template, request

from py_cari_ayat.home import router_home

@router_home.route('/') 
def index():
    return render_template(
        'home.html.j2',
        request=request,
        title='Cari Ayat',
        description='Cari Ayat is a Quran verse search engine by translating Indonesian-spell-latin query to Arabic transliteration using Soundex similarity algorithm, while the comparison algorithm is cosine similarity.'
    )