<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Monitor - README</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9fafb;
        }
        .header {
            text-align: center;
            padding: 50px 0;
            background: #343a40;
            color: white;
        }
        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
        }
        .header p {
            font-size: 1.2rem;
        }
        .section {
            padding: 40px 20px;
        }
        .section h2 {
            font-size: 2rem;
            margin-bottom: 20px;
            position: relative;
            display: inline-block;
        }
        .section h2::before {
            content: '⚡';
            position: absolute;
            left: -35px;
            animation: bounce 1.5s infinite;
        }
        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }
        .features {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            gap: 20px;
        }
        .feature {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            flex: 0 1 calc(30% - 20px);
            text-align: center;
        }
        .feature i {
            font-size: 3rem;
            color: #007bff;
            margin-bottom: 10px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
        }
        .installation {
            background: #f8f9fa;
            border-left: 5px solid #007bff;
            padding: 20px;
            margin: 20px 0;
        }
        .installation pre {
            background: #343a40;
            color: white;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        footer {
            text-align: center;
            padding: 20px;
            background: #343a40;
            color: white;
        }
    </style>
</head>
<body>

    <header class="header">
        <h1>🚀 Network Monitor</h1>
        <p>Monitoramento em tempo real de serviços de rede.</p>
    </header>

    <section class="section">
        <h2>✨ Funcionalidades</h2>
        <div class="features">
            <div class="feature">
                <i class="fas fa-search"></i>
                <h4>Monitoramento em Tempo Real</h4>
                <p>Acompanhe o status dos serviços com atualizações automáticas.</p>
            </div>
            <div class="feature">
                <i class="fas fa-cogs"></i>
                <h4>Gerenciamento de Endereços</h4>
                <p>Adicione, edite e remova serviços de forma intuitiva.</p>
            </div>
            <div class="feature">
                <i class="fas fa-lightbulb"></i>
                <h4>Feedback Visual</h4>
                <p>Ícones animados indicam o status de cada serviço.</p>
            </div>
        </div>
    </section>

    <section class="section">
        <h2>🛠️ Tecnologias</h2>
        <ul>
            <li>Backend: Flask</li>
            <li>Frontend: HTML, CSS, Bootstrap</li>
            <li>Banco de Dados: SQLite</li>
            <li>Linguagem: Python</li>
            <li>Bibliotecas: Flask-SQLAlchemy, Requests</li>
        </ul>
    </section>

    <section class="section">
        <h2>🖥️ Instalação</h2>
        <div class="installation">
            <p>Clone o repositório e instale as dependências:</p>
            <pre><code>git clone https://github.com/seu_usuario/network-monitor.git
cd network-monitor
pip install -r requirements.txt
python app.py</code></pre>
            <p>Acesse a aplicação em <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a>.</p>
        </div>
    </section>

    <footer>
        <p>Desenvolvido por <strong>Julio Morbi</strong></p>
        <p>📧 Contato: <a href="mailto:juliomorbi@gmail.com" style="color: #007bff;">seuemail@exemplo.com</a></p>
    </footer>

</body>
</html>
