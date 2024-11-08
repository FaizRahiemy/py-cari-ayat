from flask import Blueprint

router_ayat = Blueprint('router_ayat', __name__, template_folder='templates')

from py_cari_ayat.ayat import routes