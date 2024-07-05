from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Kreditur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kelayakan_usaha = db.Column(db.Float, nullable=False)
    kondisi_ekonomi = db.Column(db.Float, nullable=False)
    karakter = db.Column(db.Float, nullable=False)
    jaminan = db.Column(db.Float, nullable=False)

class Hasil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kreditur_id = db.Column(db.Integer, db.ForeignKey('kreditur.id'), nullable=False)
    skor = db.Column(db.Float, nullable=False)
