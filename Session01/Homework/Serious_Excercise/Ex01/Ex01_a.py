########## With render_template function ##########
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmii(weight,height):
    result = ""
    bmi = weight/((height/100)**2)
    if bmi < 16:
        result = "Severely underweight"
    elif 16 <= bmi < 18.5:
        result = "Underweight"
    elif 18.5 <= bmi < 25: 
        result = "Normal"
    elif 25 <= bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return render_template("bmi_calc.html",bmi = bmi,result = result)

if __name__ == '__main__':
  app.run(debug=True)