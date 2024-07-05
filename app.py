from flask import Flask, render_template, request, redirect, url_for
from models import db, Kreditur, calculate_ahp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kreditur.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    krediturs = Kreditur.query.all()
    results = calculate_ahp(krediturs)
    results_dict = {kreditur.id: result for kreditur, result in zip(krediturs, results)}
    return render_template('index.html', krediturs=krediturs, results=results_dict)

@app.route('/add', methods=['POST'])
def add_kreditur():
    nama = request.form['nama']
    kelayakan_usaha = int(request.form['kelayakan_usaha'])
    kondisi_ekonomi = int(request.form['kondisi_ekonomi'])
    karakter_nasabah = int(request.form['karakter_nasabah'])
    jaminan_nasabah = int(request.form['jaminan_nasabah'])
    new_kreditur = Kreditur(nama=nama, kelayakan_usaha=kelayakan_usaha, kondisi_ekonomi=kondisi_ekonomi,
                            karakter_nasabah=karakter_nasabah, jaminan_nasabah=jaminan_nasabah)
    db.session.add(new_kreditur)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
