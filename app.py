import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Index")

@app.route('/form')
def form():
    return render_template("form.html",  page_title="Form")


@app.route('/media')
def media():
    return render_template("media.html",  page_title="Media")
   
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)