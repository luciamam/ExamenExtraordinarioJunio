from flask import Flask,render_template 
from Forms.forms  import RegisterForm,LoginForm
from flask_bootstrap import Bootstrap4
from dotenv import load_dotenv
load_dotenv()
import os






app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
Bootstrap4(app)





@app.route('/')
def home():
    return render_template ('Home.html')



@app.route('/register')
def mostrar_register():
    form=RegisterForm()
    return render_template('Register.html',form=form)


@app.route('/register',methods=['POST'])
def register():
    return "usuario registrado "




@app.route('/login')
def mostrar_login():
    form=LoginForm()
    return  render_template('Login.html',form=form)



@app.route('/login',methods=['POST'])
def login():
    return "usuario iniciando sesion"
    



#personalizar el 404
@app.errorhandler(404)
def NotFound(mensaje):
    return render_template('NotFound.html')






if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")