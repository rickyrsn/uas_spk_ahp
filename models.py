from flask_sqlalchemy import SQLAlchemy
import numpy as np

db = SQLAlchemy()

class Kreditur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), nullable=False)
    kelayakan_usaha = db.Column(db.Integer, nullable=False)
    kondisi_ekonomi = db.Column(db.Integer, nullable=False)
    karakter_nasabah = db.Column(db.Integer, nullable=False)
    jaminan_nasabah = db.Column(db.Integer, nullable=False)

def calculate_ahp(krediturs):
    # Definisikan kriteria dan matriks perbandingan berpasangan
    criteria = ['kelayakan_usaha', 'kondisi_ekonomi', 'karakter_nasabah', 'jaminan_nasabah']
    criteria_weights = {
        'kelayakan_usaha': 0.25,
        'kondisi_ekonomi': 0.25,
        'karakter_nasabah': 0.25,
        'jaminan_nasabah': 0.25
    }

    # Matriks perbandingan berpasangan kriteria (4x4)
    pairwise_matrix = np.array([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ])

    # Normalisasi matriks perbandingan berpasangan
    col_sum = np.sum(pairwise_matrix, axis=0)
    normalized_matrix = pairwise_matrix / col_sum

    # Hitung nilai eigenvector (prioritas kriteria)
    criteria_priorities = np.mean(normalized_matrix, axis=1)

    # Hitung skor AHP untuk setiap kreditur
    results = []
    for kreditur in krediturs:
        scores = []
        for criterion in criteria:
            scores.append(getattr(kreditur, criterion) * criteria_weights[criterion])
        total_score = sum(scores)
        results.append((kreditur.nama, total_score))

    # Urutkan hasil berdasarkan skor total (skor tertinggi di atas)
    results.sort(key=lambda x: x[1], reverse=True)
    return results
