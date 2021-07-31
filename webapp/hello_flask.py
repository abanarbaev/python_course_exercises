from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask (__name__)

@app.route('/')

def hello() -> str :
    return 'Hello world from Flask'

@app.route('/search4', methods=['GET', 'POST'])

def do_search() -> str :
    #search4letters()
    return str(search4letters(request.form['phrase'], request.form['letters']))

@app.route('/entry', methods=['GET','POST'])

def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run(debug=True)

