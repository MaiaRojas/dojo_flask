from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
  
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
  return '¡Hola Mundo!' 
    
@app.route('/dojo')
def dojo():
  return "¡Dojo!" # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/say/<user>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def say_name(user):
  if isinstance(user, int):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez."
  return "¡Hola, " + user+ "!"
  
@app.route('/repeat/<times>/<word>')
def repeat_word(times, word):
  if isinstance(word, str) and  isinstance(int(times), (int)) :
    return word* int(times)

  return "¡Lo siento! No hay respuesta. Inténtalo otra vez."

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
  app.run(debug=True)    # Ejecuta la aplicación en modo de depuración


    