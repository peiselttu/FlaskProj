from flask import Flask,render_template,url_for,flash,redirect
# from pythonProj.Flask.flask_blog.form import RegisterationForm,LoginForm
from form import RegisterationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
app.config['SECRET_KEY']="this is my secret key"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default="default.jpg")
    Email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(20),nullable=False, unique=True)

    posts=db.relationship('Post',backref="author",lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.Email}','{self.image_file}')"

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50), unique=True, nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    context=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"



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
    form=RegisterationForm()
    if form.validate_on_submit():
        print('Run here')
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for("home"))
    return render_template("register.html",
                           form=form,
                           title='Registeration')

# add a login page
@app.route('/login',methods=['POST','GET'])
def login():
    formLogin=LoginForm()
    if formLogin.validate_on_submit():
        print("Running Here")
        if formLogin.email.data=='bo.pei@ufl.edu' and formLogin.password.data=="bPei*19871123":
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful, Please check the username and password',"danger")
    return render_template("login.html",
                           form=formLogin,
                           title='Login')

## directly run in python
if __name__=="__main__":
    app.run(debug=True)