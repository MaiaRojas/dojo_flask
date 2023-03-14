from flask import Flask, render_template

app = Flask(__name__)
  
@app.route('/')
def hola_mundo():
  return "Hello, world"

@app.route('/play')
def level_one():
  return render_template('index.html', times=3, color='blue')

@app.route('/play/<int:times>')
def level_two(times):
  return render_template('index.html', times=times, color='blue')


@app.route('/play/<int:times>/<string:color>')
def level_three(times, color):
  return render_template('index.html', times=times, color=color)


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
  app.run(debug=True)    # Ejecuta la aplicación en modo de depuración


    