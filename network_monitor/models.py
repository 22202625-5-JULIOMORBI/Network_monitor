from flask_sqlalchemy import SQLAlchemy

# Inicialização do SQLAlchemy (o app precisa importar isso depois)
db = SQLAlchemy()

class Address(db.Model):
    """
    Modelo para armazenar informações dos endereços monitorados.
    """
    __tablename__ = 'addresses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  # Nome do serviço/endereço
    address = db.Column(db.String(100), nullable=False)            # Endereço IP ou domínio
    port = db.Column(db.Integer, nullable=False)                  # Porta do serviço
    status = db.Column(db.String(10), default='Unknown')          # Status do monitoramento ('Online', 'Offline', etc.)

    def __repr__(self):
        return f'<Address {self.name}>'
