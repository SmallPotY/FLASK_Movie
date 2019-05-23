# -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#
# app.config['SQLALCHEMY_DATABASE_URI'] = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
#                                                                            PORT, DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'SDF-jfiJOcd'
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static" + os.sep + "uploads" + os.sep)
app.config['FC_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                    "static" + os.sep + "uploads" + os.sep + "users" + os.sep)

app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_buleprint
from app.admin import admin as admin_buleprint

app.register_blueprint(home_buleprint)
app.register_blueprint(admin_buleprint, url_prefix="/admin")  # 添加路由前缀


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
