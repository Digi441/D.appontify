from flask import Flask, render_template, session, redirect, request, flash
import pyrebase, flask_cors, traceback
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

config = {
  'apiKey': "AIzaSyAsqJvZEY77L0pN2xQajOIUyaSvXsFvnoM",
  'authDomain': "dappontify.firebaseapp.com",
  'databaseURL': "https://dappontify-default-rtdb.firebaseio.com",
 'projectId': "dappontify",
  'storageBucket': "dappontify.appspot.com",
 'messagingSenderId': "451175250127",
  'appId': "1:451175250127:web:5a7d61367ed6d21e219fba",
 'measurementId': "G-15RBVPQJR0"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app.secret_key='mPq13TTCK4iTP8FLlYspwJM8I3S40SfZ7192kg8TNU' 

@app.route('/')
def home():
    if 'user' in session:
        return render_template('index.html')
    else:
        return redirect('/login') 
        
        
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

@app.route('/create', methods=['POST', 'GET'])
def create_page():
    if 'user' in session:
        return redirect("/")
    if request.method == 'POST':
        name = request.form.get('name')
        phn = request.form.get('tel')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirmation = request.form.get('password1')

        if email is None or password is None:
            return {'message': 'Error missing email or password or phone number'}
        if password != password_confirmation:
            error_message ='Passwords do not match!'    
            return render_template("error.html", error_message=error_message)
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken']) 
            """  user_data = {
            'name': name,
            'phone_number': phn
        }"""
            """db.child('users').child(user['localId']).set(user_data)"""
            return render_template("index.html")
        except Exception as e:
             error_message = f'Error creating user: {str(e)}'
        return render_template("error.html", error_message=error_message)
    return render_template("create.html")
@app.route('/logout')
def logout():
    message = 'your have been logged'
    session.pop('user', None) 
    return render_template("logout.html", message=message)

if __name__ == "__main__":
    app.run(debug=True, port=8000)