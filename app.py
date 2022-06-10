import os
from pdb import set_trace
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import pdb


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://imperial:imperial-fdt-online-2019-colossal-shelf@imperial-2021.ckp3dl3vzxoh.eu-west-2.rds.amazonaws.com:5432/dvdrental"
db = SQLAlchemy(app)



class Inventory(db.Model):
  film_id = db.Column(db.Integer(), primary_key=True)
  inventory_id = db.Column(db.Integer(), ForeignKey('film.film_id'))
  store_id = db.Column(db.Integer())

  def __repr__(self):
    return 'Inventory ID: '+str(self.inventory_id)

class Film(db.Model):
  __tablename__ = 'film'
  film_id = db.Column(db.Integer, primary_key=True)

  title = db.Column(db.String(255), index=True, unique=True)
  description = db.Column(db.String())

  copies = relationship('Inventory')


  def __repr__(self):
    return 'FILM: title is ' + self.title




@app.route('/')
@app.route('/index')
def index():
  return "Hello, World?"





@app.route('/films')
def films():
  films = Film.query.all()

  # print(films[0].description)

  return render_template('films.html', films = films)




if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)

