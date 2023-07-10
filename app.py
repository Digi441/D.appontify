from flask import Flask, render_template, session, redirect, request, flash
import pyrebase

app = Flask(__name__)

config = {
    'apiKey': "AIzaSyAsqJvZEY77L0pN2xQajOIUyaSvXsFvnoM",
    'authDomain': "dappontify.firebaseapp.com",
    'projectId': "dappontify",
    'storageBucket': "dappontify.appspot.com",
   'messagingSenderId': "451175250127",
    'appId': "1:451175250127:web:5a7d61367ed6d21e219fba",
   'measurementId': "G-15RBVPQJR0",
    'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key='mPq13TTCK4iTP8FLlYspwJM8I3S40SfZ7192kg8TNU'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST','GET'])
def login_page():
    if('user' in session):
        return redirect("/")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user']= True
            return render_template("index.html")
        except:
            return "invalid credentials!!!!"                
    return render_template("login.html")

@app.route('/create')
def create_page():
    return render_template("create.html")

@app.route('/logout')
def logout():
    message = 'your have been logged'
    session.pop('user', None) 
    return render_template("logout.html", message=message)

if __name__ == "__main__":
    app.run(debug=True, port=8000)