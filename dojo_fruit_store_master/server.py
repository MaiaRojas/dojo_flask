from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)  
app.secret_key = 'secret' # set a secret key for security 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['GET', 'POST'])         
def checkout():
    if request.method == 'POST':
        total = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
        order = {
            'products': {
                "sb": request.form['strawberry'],
                "rb": request.form['raspberry'],
                "ap": request.form['apple'],
            },
            "f_name": request.form['first_name'],
            "l_name": request.form['last_name'],
            "s_id": request.form['student_id'],
            'total': total,
            'order_date': datetime.today().strftime('%B %d' + ' at ' + ' %I:%M:%S %p')
        }
        print(f"Cobrando a {order['f_name']} por  {total} frutas")
        session['order'] = order
        return redirect("/checkout")
    else:
        return render_template("checkout.html", order=session['order'])

@app.route('/fruits')      
def fruits():
    fruits = [
        { 'name': 'Piero Bilbao', 'img': '/static/img/strawberry.png', 'description': 'Lorem ipsumkkknksndksn', 'alt': 'strawberry' },
        { 'name': 'Abril Cristine', 'img': '/static/img/raspberry.png', 'description': 'Lorem ipsumkkknksndksn', 'alt': 'raspberry' },
        { 'name': 'Blackberry', 'img': '/static/img/blackberry.png', 'description': 'Lorem ipsumkkknksndksn', 'alt': 'apple' },
        { 'name': 'Apple', 'img': '/static/img/apple.png', 'description': 'Lorem ipsumkkknksndksn', 'alt': 'apple' }]
    return render_template("fruits.html", fruits = fruits)

if __name__=="__main__":   
    app.run(debug=True)    
