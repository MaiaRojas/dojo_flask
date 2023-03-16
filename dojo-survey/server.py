from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Maia key' # establece una clave secreta

# nuestra ruta de índice manejará la representación de nuestro formulari
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form['comment'],
            'date':  datetime.today().strftime('%B %d' + ' at ' + ' %I:%M:%S %p')
        }
        session['survey'] = data
        return redirect('result')
    else:
        return render_template('result.html', survey=session['survey'])

if __name__ == "__main__":
    app.run(debug=True)

