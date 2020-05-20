from flask import render_template,url_for,flash,redirect
from flaskblog import app
from flaskblog.form import RegisterationForm, LoginForm

#dummy data
posts=[{'author':'Corey Shafer',
        'title':'Post_1',
        'content':'First post',
        'date_posted':'April 20th 2019'},
       {'author':'Andrew Deo',
        'title':'Post_2',
        'content':'Second Post',
        'date_posted':'April 21 2019'}]

# add a home page
@app.route("/")
def home():
    # return "Hello World!" # the normal text
    # return "<h1>Home Page!</h1>" # set a larger text
    return render_template('home.html',posts=posts,title="Home Page")


# add an about page
@app.route("/about")
def about():
    # return "<h1>About Page!</h1>"
    return render_template('about.html',title="About Page")

# add an Register page
@app.route('/register',methods=['GET','POST'])
def register():
    formRegister=RegisterationForm()
    if formRegister.validate_on_submit():
        print('Run here')
        flash(f'Account created for {formRegister.username.data}!','success')
        return redirect(url_for("home"))
    return render_template("register.html",
                           form=formRegister,
                           title='Registeration')

# add a login page
@app.route('/login',methods=['POST','GET'])
def login():
    formLogin=LoginForm()
    print('out of validation...')
    if formLogin.validate_on_submit():
        print("in validation...")
        if formLogin.email.data=='bo.pei@ufl.edu' and formLogin.password.data=="bPei*19871123":
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful, Please check the username and password',"danger")
    return render_template("login.html",
                           form=formLogin,
                           title='Login')
