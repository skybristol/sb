from flask import Flask, render_template, redirect, request, url_for

from datetime import datetime
import markdown

app = Flask(__name__)

def convert_md(article):
    with open(f'articles/{article}.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
        return html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('render_md.html', content=convert_md('about'))

@app.route('/writing.html')
def writing():
    return render_template('render_md.html', content=convert_md('writing'))

@app.route('/code.html')
def code():
    return render_template('render_md.html', content=convert_md('code'))

