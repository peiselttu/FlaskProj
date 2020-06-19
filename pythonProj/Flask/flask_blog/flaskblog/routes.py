from flask import render_template,url_for,flash,redirect,request
from flaskblog import app, bcrypt,db
from flaskblog.form import RegisterationForm, LoginForm
from flaskblog.model import User,Post
from flask_login import login_user,logout_user,current_user,login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    formRegister=RegisterationForm()
    if formRegister.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(formRegister.password.data).decode('utf-8')
        user=User(username=formRegister.username.data,Email=formRegister.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        print(User.query.all())
        flash(f'Your account has been registered successfully, you are able to log in!','success')
        return redirect(url_for("login"))
    return render_template("register.html",
                           form=formRegister,
                           title='Registeration')

# add a login page
@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    formLogin=LoginForm()
    if formLogin.validate_on_submit():
        user=User.query.filter_by(Email=formLogin.email.data).first()
        if user and bcrypt.check_password_hash(user.password,formLogin.password.data):
            login_user(user,remember=formLogin.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful, Please check the username and password',"danger")
    return render_template("login.html",
                           form=formLogin,
                           title='Login')

# add a logout link
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title='Account')
