from flask import Flask, request, render_template, url_for, flash, redirect
import re

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'a_super_secret_key!'

@app.route('/', methods = ['GET', 'POST'])
def index():
    errors = 0
    username=''
    email=''
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        verifypassword = request.form['verifypassword']
        email = request.form['email'].strip()

        # validation 1: Username and password are valid. i.e. 3-20 characters long
        for field,value in [('username',username),('password',password)]:
            if not 3 <= len(value)<= 20:
                flash('Invalid {}'.format(field),field)
                errors += 1
                
        # validation 2: password verification
        if verifypassword != password:
            flash("Passwords don't match",'verifypassword')
            errors += 1
            
        # validation 3: email
        email_pattern = '[^. @]+@+[^. @]+.+[^. @]'
        if email and not (3 <= len(email) <= 20 and re.match(email_pattern,email)):
            flash("Invalid email address",'email')
            errors += 1
            

        if errors > 0:
            return render_template('form.html',
                            username = username,
                            email = email
                           )
        else:
            return render_template('welcome.html',
                            username = username
                           )

    else:
        return render_template('form.html',
                            username = username,
                            email = email
                           )

app.run()