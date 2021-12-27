from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '!ng3[@'

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Information Collected")
#     print(request.form)
#     return redirect('/')

@app.route('/process_form', methods=['POST'])
def process_form():
    session['sesfirst']=request.form['first_name']
    session['seslast']= request.form['last_name']
    session['seslocal']= request.form['location']
    session['seschar']= request.form['character']
    session['sestext']= request.form['episode']
    return redirect('/result')

@app.route('/result')
def result():
    result='data'
    return render_template('results.html', first= session['data']['first_name'], last= session['data']['last_name'],location= session['data']['location'], character= session['data']['character'], favorite= session['data']['episode'])

if __name__=="__main__":
    app.run(debug=True)