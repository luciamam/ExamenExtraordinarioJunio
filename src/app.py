from flask import Flask,render_template ,flash,request,redirect,url_for
from Forms.forms  import RegisterForm,LoginForm
from flask_bootstrap import Bootstrap4
from dotenv import load_dotenv
from pymongo import MongoClient
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import JWTManager,get_jwt_identity ,jwt_required
import json
from bson  import ObjectId 
load_dotenv()
import os






app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
Bootstrap4(app)
client=MongoClient("mongodb://localhost:27017/")
db=client["ExamenExtraordinarioJunio"]
usuarios=db["usuarios"]
jwt=JWTManager(app)





@app.route('/')
def home():
    return render_template ('Home.html')



@app.route('/register')
def mostrar_register():
    form=RegisterForm()
    return render_template('Register.html',form=form)


@app.route('/register',methods=['POST'])
def register():
    datos=request.form
    #por seguridad , en caso de hacerse uno con la base de datos voy hashear la constraseña 
    #para no guardarla en texto plano 
    usuario={
        "name":datos["name"],
        "email":datos["email"],
        "password":generate_password_hash(datos["password"])
    }
    docuemento_usuario=usuarios.insert_one(usuario)

    return redirect(url_for('perfil'))



@app.route('/login')
def mostrar_login():
    form=LoginForm()
    return  render_template('Login.html',form=form)


@app.route('/login',methods=['POST'])
def login():
    datos=request.form
    usuario_recuperado= usuarios.find_one({"email":datos["email"]})
    if usuario_recuperado:
        if check_password_hash(usuario_recuperado["password"],datos["password"]):
            return redirect(url_for('perfil'))
        else :
            flash("contraseña incorrecta","info")
            return  redirect(url_for('mostrar_login'))
    else:
        return redirect(url_for("register"))




# para poder recuperar el nombre del usuario voy a usar el jwt token  y voy a proteger esta ruta 
@app.route('/perfil')
@jwt_required(locations=['cookies'])
def perfil():
    return "bienvenido usuario "


#personalizar el 404
@app.errorhandler(404)
def NotFound(mensaje):
    return render_template('NotFound.html')


#capturar el error del 401

@jwt.unauthorized_loader
def capturar(mensaje):
    return redirect(url_for('mostrar_register'))



if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")