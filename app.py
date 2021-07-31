from re import DEBUG
from flask import Flask, render_template, request
import joblib

#instance of an App
app = Flask(__name__)

model = joblib.load('dib_79.pkl')

@app.route('/')
def welcome():
    return 'Hello World'


@app.route('/home')
def home():
    #return 'Welcome to Home Page'
    return render_template('home.html')

@app.route('/Contact', methods=['POST'])
def Contact():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])

    if output[0] == 1:
        out1 = 'Diabetic..!!'
    else:
        out1 = 'not Diabetic..!'

    #return 'Contact Page'    
    return render_template('contact.html', Predicted_Text =f'The Person is {out1}')                                                   

if __name__ == '__main__':
    app.run(debug=True)

