from flask import Flask
import logging
import os
import sys

from config import Config
from py_cari_ayat.models.base import db

def setup_logging():
    if os.environ.get('FLASK_ENV') and os.environ.get('FLASK_ENV') == 'development':
        logging.basicConfig(filename='pycariayat.log', level=logging.DEBUG)
    else:
        logging.basicConfig(filename='pycariayat.log', level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static')
    app.config.from_object(Config)
    setup_logging()
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from py_cari_ayat.home import router_home
    app.register_blueprint(router_home)
    from py_cari_ayat.surat import router_surat
    app.register_blueprint(router_surat, url_prefix='/surat')
    from py_cari_ayat.ayat import router_ayat
    app.register_blueprint(router_ayat, url_prefix='/ayat')

    return app