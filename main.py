from flask import Flask, request, render_template, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        errors = {
            'username':'',
            'password':'',
            'verify':''
        }
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verifypassword']
        email = request.form['email']

        # verify 1: all required fields are provided
        for field in [username,password,verify]:
            if not field:
                errors[field] = 1
        # verify 2: username and password length


    return render_template('form.html')

app.run()