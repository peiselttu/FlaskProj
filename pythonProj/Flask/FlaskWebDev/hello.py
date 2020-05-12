from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
bootstrap=Bootstrap(app)

# Define a secret_key
app.config['SECRET_KEY']="bo's Flasky"

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
@app.route("/",methods=["GET","POST"])
def index():
    form=NameForm()
    old_name = session.get('name')
    if form.validate_on_submit():
        print('old_name',old_name)
        print(form.name.data)
        if old_name is not None and old_name!=form.name.data:
            flash("The input name is inconsistent")
        session['name']=form.name.data
        form.name.data=""
        return redirect(url_for("index"))
    return render_template("index.html",form=form,name=session.get('name'))


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