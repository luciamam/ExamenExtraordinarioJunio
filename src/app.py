from flask import Flask,render_template 


from dotenv import load_dotenv
load_dotenv()
import os






app=Flask(__name__)

app.config['SECRET_KEY']=os.getenv('SECRET_KEY')





@app.route('/')
def home():
    return "estoy en la ruta raiz "



@app.route('/register')
def mostrar_register():
    return "soy la ruta register"


@app.route('/login')
def mostrar_login():
    return "soy la ruta login "


#personalizar el 404
@app.errorhandler(404)
def NotFound(mensaje):
    return render_template('NotFound.html')






if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")