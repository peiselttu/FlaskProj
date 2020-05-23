from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import main
from . forms import NameForm
from .. import db
from ..models import User

# @main.route('/',methods=['GET','POST'])
# def index():
#     form=NameForm()
#     if form.validate_on_submit():
#         user=User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user=User(username=form.name.data)
#             db.session.add(user)
#             session['known']=False
#         else:
#             session['known']=True
#         session['name']=form.name.data
#         form.name.data=""
#         return redirect(url_for('.index'))
#     return render_template('index.html',form=form,
#                            name=session.get('name'),
#                            known=session.get('known',False))

@main.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    uName=session.get('uName')
    if form.validate_on_submit():
        if uName==form.name.data:
            return redirect(url_for('.index'))
        else:
            session['uName']=form.name.data
    return render_template('index.html',name=session.get('uName'),form=form)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    # page = request.args.get('page', 1, type=int)
    # pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
    #     page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    #     error_out=False)
    # posts = pagination.items
    return render_template('user.html',user=user)
    # return render_template('user.html', user=user, posts=posts,
    #                        pagination=pagination)