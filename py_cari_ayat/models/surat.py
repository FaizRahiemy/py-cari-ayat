from py_cari_ayat.models.base import db
from py_cari_ayat.models.ayat import Ayat # type: ignore

class Surat(db.Model):
    __tablename__: str = 'surat'
    id: int = db.Column(db.Integer, primary_key=True)
    surat: str = db.Column(db.String(255))
    juz: str = db.Column(db.String(255))
    ayats = db.relationship('Ayat', backref='surat')

    def __repr__(self):
        return f'<Surat "{self.surat}">'