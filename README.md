
# 🚀 Network Monitor

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Flask](https://img.shields.io/badge/Flask-v2.0-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**Network Monitor** é uma aplicação web para monitoramento em tempo real de serviços de rede. Ideal para acompanhar o status de conexões, como servidores e serviços críticos.

## ✨ Funcionalidades

- 🔍 **Monitoramento em Tempo Real**: Verifique a conectividade de serviços por IP ou domínio.
- ⚙️ **Gerenciamento de Endereços**: Adicione, edite ou remova endereços monitorados.
- 💡 **Feedback Visual**: Ícones animados para representar o status dos serviços.
- 📊 **Interface Responsiva**: Adaptada para dispositivos móveis e desktop.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Banco de Dados**: SQLite
- **Linguagem**: Python
- **Bibliotecas**: Flask-SQLAlchemy, Requests

## 🖥️ Instalação e Configuração

### Pré-requisitos

- Python 3.7 ou superior
- Gerenciador de pacotes `pip`

### Passos para Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu_usuario/network-monitor.git
   cd network-monitor
Instale as dependências:

pip install -r requirements.txt
Inicialize o banco de dados:

python
from app import db
db.create_all()
exit()

Inicie o servidor:

python app.py
Acesse a aplicação no navegador em http://127.0.0.1:5000.

📂 Estrutura do Projeto

├── app.py               # Arquivo principal da aplicação
├── models.py            # Modelos para o banco de dados
├── templates/           # Arquivos HTML para renderização
│   ├── base.html        # Template base
│   ├── monitor.html     # Página principal de monitoramento
│   ├── endereco.html    # Gerenciamento de endereços
│   ├── add_edit.html    # Formulário de adicionar/editar
├── static/              # Arquivos estáticos
│   ├── css/
│   │   └── styles.css   # Estilo personalizado
│   ├── js/
│   │   └── script.js    # Atualizações de status em tempo real
│   └── icons/           # Ícones para status
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo

🎨 Ícones de Status

Online:
Offline:
Instável:

Os ícones animados são exibidos automaticamente de acordo com o status do serviço.

🔧 Como Usar
Acesse a aba Endereços para gerenciar os serviços monitorados.
Adicione os dados: Nome, Endereço (IP ou domínio) e Porta.
Acompanhe o status em tempo real na aba Monitorar.

🤝 Contribuição
Contribuições são bem-vindas! Siga os passos:

Faça um fork do repositório.
Crie uma branch para sua feature: git checkout -b minha-feature.
Envie um pull request explicando suas mudanças.

📄 Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais informações.

Desenvolvedor: Seu Nome
📧 Contato: juliomorbi@gmail.com
