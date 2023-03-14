from flask import Flask, render_template

app = Flask(__name__)
  

@app.route('/')
def level_one():
  return "Hello a table"

@app.route('/list')
def level_two():
  users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ]
  return render_template('index.html', users=users)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
  app.run(debug=True)    # Ejecuta la aplicación en modo de depuración


    