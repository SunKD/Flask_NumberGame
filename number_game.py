from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key="secret"

@app.route('/')
def index():
    if 'ranNum' not in session:
        session['ranNum'] = random.randrange(0, 101)
    if 'result' not in session:
        session['result'] = 4
    print session['ranNum']
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def guess():
    guess = int(request.form['userInput'])
    if session['ranNum'] > guess:
        session['result'] = 1
    elif session['ranNum'] < guess:
        session['result'] = 2
    else:
        session['result'] = 0
    
    print session['ranNum']
    return redirect('/')

@app.route('/playAgain', methods=['POST'])
def playAgain():
    session.clear()
    return redirect('/')
    
app.run(debug=True)