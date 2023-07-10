import pyrebase 

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

email='fortesting@gmail.com'
password='123456'

#user = auth.create_user_with_email_and_password(email, password)

user = auth.sign_in_with_email_and_password(email, password)
#print("User:", user['localId'])  # The local ID of the new account

auth.send_email_verification(user['id_token'])

auth.send_password_reset_email(email)