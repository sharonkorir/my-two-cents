from flask import render_template, request, redirect, url_for, abort
from . import main
from ..request import get_quote
from flask_login import login_required, current_user
from ..models import User, Post, Comment
from .forms import UpdateProfile, PostForm, CommentForm
from .. import db, photos

@main.route('/')
def index():
    title = 'My Two Cents'
    quote = get_quote()
    post_id = Post.id
    posts = Post.get_posts(post_id)
    return render_template('index.html', title=title, quote=quote, posts = posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_profile.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/create_post', methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
  
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = current_user
        new_post = Post(title=title, content=content, user_id = current_user._get_current_object().id)
        new_post.save_post()
        return redirect(url_for('main.index'))

    return render_template('new_post.html', form=form)

@main.route('/comment/<int:post_id>', methods = ['GET','POST'])
@login_required
def new_comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    related_comments = Comment.get_comments(post_id)
    user_id = post.user_id
    user = User.query.filter_by(id = user_id).first()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, post_id = post_id, user_id = current_user.get_id())
        new_comment.save_comment()
        return redirect(url_for('.new_comment',post_id = post_id))

    return render_template('new_comment.html', comment_form=form, posts = post, comments = related_comments, user = user)