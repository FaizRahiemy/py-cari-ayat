from py_cari_ayat.models.base import db
from py_cari_ayat.models.kata import Kata

class Ayat(db.Model):
    __tablename__: str = 'ayat'
    id: int = db.Column(db.Integer, primary_key=True)
    surat_id: int = db.Column(db.Integer, db.ForeignKey('surat.id'), nullable=False)
    ayat: int = db.Column(db.Integer)
    ayat_latin: str = db.Column(db.Text)
    ayat_arab: str = db.Column(db.Text)

    def __repr__(self):
        return f'<Ayat "{self.id}">'
    
    @property
    def katas(self) -> list[Kata]:
        katas: list[Kata] = []
        for idx, kata in enumerate(self.ayat_latin.split(' ')):
            katas.append(Kata(kata, str(idx + 1), self.surat.surat, self.surat_id, self.ayat)) # type: ignore

        return katas