import os
import yaml

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLITE_HOST: str = 'cariayat.db'
    os.path.join(basedir, 'config.yaml')
    with open(os.path.join(basedir, 'config.yaml'),"r") as config_file:
        config_file_content = yaml.safe_load(config_file)
        if 'SQLITE_HOST' in config_file_content:
            SQLITE_HOST = config_file_content['SQLITE_HOST'] # type: ignore
    SQLALCHEMY_DATABASE_URI: str = f'sqlite:///cariayat.db'
    # SQLALCHEMY_DATABASE_URI: str = f'sqlite:///{SQLITE_HOST}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False