#!/usr/bin/env python
import os
import json
from flask import Flask,render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
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
