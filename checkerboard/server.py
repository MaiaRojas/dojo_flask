from flask import Flask, render_template

app = Flask(__name__)
  

@app.route('/')
def level_one():
  return render_template('checkerboard.html', xsize=8, ysize=8, color1="red", color2="black")

@app.route('/<int:xsize>')
def level_two(xsize):
  return render_template('checkerboard.html', xsize=xsize, ysize=8, color1="red", color2="black")


@app.route('/<int:xsize>/<int:ysize>')
def level_three(xsize, ysize):
  return render_template('checkerboard.html', xsize=xsize, ysize=ysize, color1="red", color2="black")

@app.route('/<int:xsize>/<int:ysize>/<string:color1>/<string:color2>')
def level_four(xsize, ysize, color1, color2):
  return render_template('checkerboard.html', xsize=xsize, ysize=ysize, color1=color1, color2=color2)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
  app.run(debug=True)    # Ejecuta la aplicación en modo de depuración


    