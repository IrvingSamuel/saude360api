from flask import Flask
from routes.main import main_bp
import config

app = Flask(__name__)
app.config.from_object(config.Config)

# Registrar rotas
app.register_blueprint(main_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)