from flask import Flask, render_template, request, redirect, session
import random  # import the random module

app = Flask(__name__)
app.secret_key = 'Maia key' # establece una clave secreta

# nuestra ruta de índice manejará la representación de nuestro formulari
@app.route('/')
def index():
    if 'game_key' not in session:
        session['game_key'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    session['game_input'] = int(request.form['game'])
    return redirect("/")

@app.route('/clear')
def clear():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

