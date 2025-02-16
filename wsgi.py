from flask import Flask
from flask_elastic import app as app_bp
from dotenv import load_dotenv

load_dotenv()
application = Flask("flask_elastic")
application.register_blueprint(app_bp)


if __name__ == "__main__":
    application.run(debug=True)
