from flask import Flask
from routes.main import main_bp
import config
import os

app = Flask(__name__)
app.config.from_object(config.Config)

# Registrar rotas
app.register_blueprint(main_bp, url_prefix="/api")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Pega a porta definida pelo Railway
    app.run(host="0.0.0.0", port=port)