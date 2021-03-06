from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import os

datadir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
bootstrap=Bootstrap(app)


# Define a secret_key
app.config['SECRET_KEY']="bo's Flasky"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(datadir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref="role",lazy='dynamic')

    def __repr__(self):
        return '<Role %r>'%self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>'%self.username

class NameForm(FlaskForm):
    name=StringField("What's your name?",validators=[DataRequired()])
    submit=SubmitField('Submit')


# 刷新网页时，会弹出警告信息提示框
# @app.route('/',methods=['GET','POST'])
# def index():
#     name=None
#     form = NameForm()
#     if form.validate_on_submit():
#         name=form.name.data
#         form.name.data=""
#     return render_template("index.html",form=form,name=name)

# @app.route('/',methods=['GET','POST'])
# def index():
#     form=NameForm()
#     if form.validate_on_submit():
#         session['name']=form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html',form=form,name=session.get('name'))

# information submission with a flashing message
# @app.route("/",methods=["GET","POST"])
# def index():
#     form=NameForm()
#     old_name = session.get('name')
#     if form.validate_on_submit():
#         print('old_name',old_name)
#         print(form.name.data)
#         print(form.name.data==old_name)
#         if old_name is not None and old_name==form.name.data:
#         # if form.name.data=="peibo":
#             flash(f"The input name is inconsistent",'danger')
#             # session['name']=form.name.data
#             form.name.data=""
#             return redirect(url_for("user",name=session.get('name')))
#     return render_template("index.html",name=session.get('name'),form=form)

'''
An updated index
'''
@app.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            session['known']=False
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=""
        return redirect(url_for('index'))
    return render_template('index.html',form=form,
                           name=session.get('name'),
                           known=session.get('known',False))


@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500



if __name__=="__main__":
    app.run(debug=True)