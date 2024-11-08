from py_cari_ayat.models.base import db

class Ayat(db.Model):
    __tablename__: str = 'ayat'
    id: int = db.Column(db.Integer, primary_key=True)
    surat_id: int = db.Column(db.Integer, db.ForeignKey('surat.id'), nullable=False)
    ayat: int = db.Column(db.Integer)
    ayat_latin: str = db.Column(db.Text)
    ayat_arab: str = db.Column(db.Text)

    def __repr__(self):
        return f'<Ayat "{self.id}">'