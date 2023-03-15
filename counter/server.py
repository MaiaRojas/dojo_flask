from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Maia key' # establece una clave secreta

# nuestra ruta de índice manejará la representación de nuestro formulari
@app.route('/')
def index():
    if 'counter' in session:
        print('la llave existe!')
        session['counter'] = session.get('counter', 0) + 1
    else:
        print("la llave 'key_name' NO existe")
        session['counter'] = 0
    return render_template("index.html")

@app.route('/moreVisit')
def moreVisit():
    print("Got Post Info")
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('counter')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

