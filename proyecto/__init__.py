from flask import Flask



import sys
sys.path.append(".")

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/namedb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'your secret key'

from proyecto.controllers.ProyectoController import  Route
app.register_blueprint(Route, url_prefix='/')