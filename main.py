from flask import Flask, render_template, request,session,redirect,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import json
import math
import os
from datetime import datetime

with open('config.json', 'r') as c:
    parameter = json.load(c)["parameter"]


local_server = True
app = Flask(__name__)
app.secret_key='super-secret-key'

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = parameter['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = parameter['prod_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    pin = db.Column(db.String(8), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    message = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Pdfs(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    img_file = db.Column(db.String(25), nullable=False)
    file = db.Column(db.String(50), nullable=False)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pdf")
def pdf():
    pdfs = Pdfs.query.filter_by().all()
    return render_template("pdf.html",parameter=parameter,pdfs=pdfs)


app.config['upload_loc'] = "C:/Users/het/PycharmProjects/OnlineLerning/static/client"
@app.route("/get-pdf/<filename>")
def get_pdf(filename):
    return send_from_directory(
        app.config['upload_loc'],filename=filename,as_attachment=True
    )


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        uname = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        pin = request.form.get('pin')
        country = request.form.get('country')
        message = request.form.get('message')
        entry = Contacts(uname=uname , email = email , phone_no = phone , pin = pin , country = country , message = message , date= datetime.now())
        db.session.add(entry)
        db.session.commit()
#       mail.send_message('New message from '+name,
#                          sender=email,
#                          recipients =params['gmail-user'],
#                          body = message + '\n' + phone
#                          )
    return render_template('contact.html')

app.run(debug=True)