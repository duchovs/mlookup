import os
from flask import Flask
from bs4 import BeautifulSoup
from mlookup import *

app = Flask(__name__)
soup = BeautifulSoup('<title>NULL</title><h1>info</h1><img src="NULL" style="width:800px;height:1200px;"></img>', 'html.parser')

@app.route('/movie/<title>')
def page(title):
# can't pass by reference so return poster img for now    
    info = queue_movie(title)
    
    soup.title.string.replace_with(title)
    soup.h1.string.replace_with(info[0])
    soup.img['src'] = info[1]
    return str(soup)

if '__main__' == __name__:
    app.run(host='0.0.0.0')