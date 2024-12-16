from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import threading
import socket
import time

# Configurações da aplicação
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///network_monitor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de dados
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), default='Unknown')

# Função para testar conexão
def test_connection(address, port):
    try:
        with socket.create_connection((address, int(port)), timeout=5):
            return 'Online'
    except (socket.timeout, ConnectionRefusedError, OSError):
        return 'Offline'

@app.route('/')
def index():
    return redirect(url_for('monitor'))

@app.route('/monitor')
def monitor():
    addresses = Address.query.all()
    return render_template('monitor.html', addresses=addresses)

@app.route('/check_status', methods=['POST'])
def check_status():
    addresses = Address.query.all()
    statuses = {}
    for address in addresses:
        status = test_connection(address.address, address.port)
        address.status = status
        statuses[address.id] = status
    db.session.commit()
    return jsonify(statuses)

@app.route('/endereco')
def endereco():
    addresses = Address.query.all()
    return render_template('endereco.html', addresses=addresses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        port = request.form['port']

        new_address = Address(name=name, address=address, port=port)
        try:
            db.session.add(new_address)
            db.session.commit()
            flash('Endereço adicionado com sucesso!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Nome já existente!', 'danger')
            return redirect(url_for('add'))

    return render_template('add_edit.html', mode='add')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    address = Address.query.get_or_404(id)
    if request.method == 'POST':
        address.name = request.form['name']
        address.address = request.form['address']
        address.port = request.form['port']

        try:
            db.session.commit()
            flash('Endereço atualizado com sucesso!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Nome já existente!', 'danger')

    return render_template('add_edit.html', address=address, mode='edit')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    address = Address.query.get_or_404(id)
    db.session.delete(address)
    db.session.commit()
    flash('Endereço removido com sucesso!', 'success')
    return redirect(url_for('index'))

# Monitoramento em background
def monitor_background():
    while True:
        with app.app_context():
            for address in Address.query.all():
                address.status = test_connection(address.address, address.port)
            db.session.commit()
        time.sleep(35)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    threading.Thread(target=monitor_background, daemon=True).start()
    app.run(host='0.0.0.0', debug=True)
