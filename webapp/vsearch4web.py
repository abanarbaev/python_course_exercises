from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask (__name__)

def log_request(req:'flask_request', res:str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep=' | ')
    

@app.route('/search4', methods=['POST'])

def do_search() -> 'html':
    phrase=request.form['phrase']
    letters=request.form['letters']
    results=str(search4letters(phrase, letters))
    title='Here are your results!'
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           the_title=title,)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!',)

@app.route('/viewlog')

def view_log() -> 'html':
    cont=[]
    with open('vsearch.log') as log:
        for line in log:
            cont.append([])
            for item in line.split('|'):
                cont[-1].append(escape(item))
    titles=('Form Data', 'Remote Addr', 'User Agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=cont,)


if __name__=='__main__':
    app.run(debug=True)
