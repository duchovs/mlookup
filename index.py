import os
from flask import Flask
from mlookup import *

app = Flask(__name__)
# routing the decorator function hello_name
@app.route('/movie/<title>')
def page(title):
    queue_movie(title)
    return "<title>"+title+"</title><img src=\""+get_poster(get_dict(search_movie(title)))+"\">"

if '__main__' == __name__:
    app.run(host='0.0.0.0')