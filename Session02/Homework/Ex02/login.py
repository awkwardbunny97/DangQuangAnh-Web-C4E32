from flask import Flask, render_template , request, redirect,url_for
app = Flask(__name__)

@app.route('/sucesss')
def success_login():
    return "Login Success!"

@app.route('/fail')
def fail_login():
    return "Login Failed!"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'QuangAnh' or request.form['password'] != 'MindXC4E':
            return redirect(url_for('fail_login'))
        else:
            return redirect(url_for('success_login'))
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
