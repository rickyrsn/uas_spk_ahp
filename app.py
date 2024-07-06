from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Kreditur  # Import db dan model Kreditur dari models.py
from ahpy import Compare

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
migrate = Migrate(app, db)  # Inisialisasi Flask-Migrate

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    kreditur_list = Kreditur.query.all()
    results = []
    process_details = []
    if kreditur_list:
        data = []
        for kreditur in kreditur_list:
            data.append({
                'nama': kreditur.nama,
                'kelayakan_usaha': kreditur.kelayakan_usaha,
                'kondisi_ekonomi': kreditur.kondisi_ekonomi,
                'karakter': kreditur.karakter,
                'jaminan': kreditur.jaminan
            })

        # Mengubah cara memasukkan data perbandingan untuk AHP
        pairwise_comparisons = {
            ('Kelayakan Usaha', 'Kondisi Ekonomi'): 0.3333333333333333,
            ('Kelayakan Usaha', 'Karakter'): 0.3333333333333333,
            ('Kelayakan Usaha', 'Jaminan'): 0.2,
            ('Kondisi Ekonomi', 'Karakter'): 1,
            ('Kondisi Ekonomi', 'Jaminan'): 0.3333333333333333,
            ('Karakter', 'Jaminan'): 0.3333333333333333
        }

        # Initialize Compare object with the correct arguments
        ahp = Compare(name="KrediturComparison", comparisons=pairwise_comparisons)
        priority_weights = ahp.target_weights

        for kreditur in data:
            score = (
                kreditur['kelayakan_usaha'] * priority_weights['Kelayakan Usaha'] +
                kreditur['kondisi_ekonomi'] * priority_weights['Kondisi Ekonomi'] +
                kreditur['karakter'] * priority_weights['Karakter'] +
                kreditur['jaminan'] * priority_weights['Jaminan']
            )
            results.append({
                'nama': kreditur['nama'],
                'kelayakan_usaha': kreditur['kelayakan_usaha'],
                'kondisi_ekonomi': kreditur['kondisi_ekonomi'],
                'karakter': kreditur['karakter'],
                'jaminan': kreditur['jaminan'],
                'skor': score
            })

        results.sort(key=lambda x: x['skor'], reverse=True)
        
        # Add process details for each step
        process_details = {
            'pairwise_comparisons': pairwise_comparisons,
            'priority_weights': priority_weights,
            'data': data
        }

    return render_template('index.html', kreditur_list=kreditur_list, results=results, process_details=process_details)

@app.route('/input', methods=['POST'])
def input_data():
    nama = request.form['nama']
    kelayakan_usaha = request.form['kelayakan_usaha']
    kondisi_ekonomi = request.form['kondisi_ekonomi']
    karakter = request.form['karakter']
    jaminan = request.form['jaminan']
    
    new_kreditur = Kreditur(nama=nama, kelayakan_usaha=kelayakan_usaha, kondisi_ekonomi=kondisi_ekonomi, karakter=karakter, jaminan=jaminan)
    db.session.add(new_kreditur)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
