import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Index")

@app.route('/form')
def form():
    return render_template("i.html")


@app.route('/media')
def media():
    return render_template("media.html",  page_title="M")
   
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)