from flask import Flask, render_template,redirect
app = Flask(__name__)


@app.route('/about-me')
def about_me():
    my_information = {
        'Name' : 'Dang Quang Anh',
        'Work' : 'Product Research and Development',
        'School' : 'University of Transportation and Communication',
        'Hobbies' : 'Hangout with friends',
    }
    return render_template('aboutme.html', data = my_information)

@app.route('/school')
def direct_mindx():
    return redirect("https://mindx.edu.vn/", code=302)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 