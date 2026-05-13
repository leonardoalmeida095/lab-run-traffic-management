import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # Lê a variável de ambiente injetada pelo Cloud Run. O padrão é 'dev-local'
    version = os.environ.get("APP_VERSION", "dev-local")
    
    html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f0f8ff;">
            <h1>🚀 Teste de Tráfego Cloud Run</h1>
            <h2>Versão do Preview: <span style="color: green;">{version}</span></h2>
        </body>
    </html>
    """
    return html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)