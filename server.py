from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'yoo'

@app.route('/')
def index():
    if 'views' in session:
        session['views'] += 1
    else:
        session['views'] = 1
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0

    return render_template("counter.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug= True) 