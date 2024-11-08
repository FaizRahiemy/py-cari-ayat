from flask import Blueprint

router_surat = Blueprint('router_surat', __name__, template_folder='templates')

from py_cari_ayat.surat import routes # type: ignore