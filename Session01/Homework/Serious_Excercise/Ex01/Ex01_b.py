########## Without render_template function ##########
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def bmii(weight,height):
    result = ""
    bmi = weight/((height/100)**2)
    if bmi < 16:
        result = "Your BMI:" + str(bmi) + " | Severely underweight"
    elif 16 <= bmi < 18.5:
        result = "Your BMI:"+str(bmi)+" | Underweight"
    elif 18.5 <= bmi < 25:
        result = "Your BMI:"+str(bmi)+" | Normal"
    elif 25 <= bmi < 30:
        result = "Your BMI:"+str(bmi)+" | Overweight"
    else:
        result = "Your BMI:"+str(bmi)+" | Obese"
    return result

if __name__ == '__main__':
  app.run(debug=True)
 