from flask import Blueprint

router_home = Blueprint('router_home', __name__, template_folder='templates')

from py_cari_ayat.home import routes