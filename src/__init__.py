from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .routes.index import views

  app.register_blueprint(views, url_prefix='/')
  
  return app

def create_database(app):
  if not path.exist('src/' + DB_NAME):
    db.create_all(app=app)
    print('Created Database!')