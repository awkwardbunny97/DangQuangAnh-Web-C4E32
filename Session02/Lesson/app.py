from flask import Flask, render_template , request, redirect,url_for
app = Flask(__name__)

data = [
        {
            'name': "Chicken Rice",
            "price": 10000
        },
        {
            "name": "Beef Rice",
            "price": 20000
        },
        {
            "name": "Pork Rice",
            "price": 50000
        }
    ]

@app.route('/')
def menu_food():
    
    return render_template("index.html", data=data)

@app.route('/', methods = ['POST'])
def post_dish():
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    data.append ({
        "name" : dish_name,
        "price" : dish_price
    })
    return redirect(url_for('menu_food'))
    # return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
