#!/usr/bin/env python
import os
import json
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
db = SQLAlchemy(app)
 
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    
    def __init__(self,title,created_time,category_id,content):
        self.title = title
        self.created_time = created_time
        self.category_id = category_id
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return '<Category %r>' % self.name

db.create_all()
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')

db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()

@app.route('/')
def index():
    AllTitle = []
    path = '/home/shiyanlou/files'
    os.chdir(path)
    for root,dirs,names in os.walk(path):
        for name in names:
            f1 = open(name,encoding='utf-8')
            f = json.load(f1)
            AllTitle.append(f['title'])
    return render_template('index.html',result=AllTitle)
@app.route('/files/<filename>')
def file(filename):
        path = '/home/shiyanlou/files'
        os.chdir(path)
        filename1 = filename+'.json'
        if os.path.exists(filename1):
            f1 = open(filename1,encoding='utf-8')
            f = json.load(f1)
            return render_template('file.html',result=f['content'])
        else:
            return render_template('404.html',result=filename)
if __name__ == '__main__':
    app.run()
