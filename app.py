import datetime
from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_mysqldb import MySQL
import jwt
from routes.main_routes import main_routes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'erp_escolar'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



# Registra as rotas principais
app.register_blueprint(main_routes)

# Restante do seu código...

if __name__ == '__main__':
    app.run(debug=True)
