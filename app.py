from flasgger import Swagger
from flask import Flask, send_from_directory
from flask.blueprints import Blueprint
import config
import routes
from models import db
from flask_migrate import Migrate
import flask_excel
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__, static_url_path='', static_folder='FE/techcollins/dist')
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
bcrypt = Bcrypt(app)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config["JWT_SECRET_KEY"] = "super-secret"
CORS(app)
jwt = JWTManager(app)

app.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "Application API",
    "specs": [
        {
            "version": "0.0.1",
            "title": "Application API",
            "endpoint": "spec",
            "route": "/application/spec",
            "rule_filter": lambda rule: True,  # all in
        }
    ],
    "static_url_path": "/apidocs",
}

Swagger(app)
app.debug = config.DEBUG
app.config['SECRET_KEY'] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['UPLOAD_FOLDER'] = "./folders/"
db.init_app(app)
db.app = app

db.create_all()
migrate = Migrate(app, db)

flask_excel.init_excel(app)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=True)
