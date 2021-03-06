
from flask import render_template, request, redirect, url_for, abort, flash
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
    posts = Post.get_posts()
    posts.reverse()
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
        #author = form.author.data
        #user_id = current_user
        user = current_user.id
        new_post = Post(title=title, content=content, user_id = current_user._get_current_object().id)
        new_post.save_post()

        flash("Your post has been created successfully!")
        return redirect(url_for('main.index'))
    
    return render_template('new_post.html', form=form)

#view post
@main.route('/post/<int:post_id>', methods = ['GET','POST'])
@login_required
def new_comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    related_comments = Comment.get_comments(post_id)
    user_id = current_user.get_id()
    #user_id = related_comments.users.id
    user = User.query.filter_by(id = user_id).first()
    #user = User.query.filter_by(id = user_id).first()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, post_id = post_id, user_id = current_user.get_id())
        comment_user = User.query.filter_by(id = new_comment.user_id).first()
        new_comment.save_comment()
        return redirect(url_for('.new_comment',post_id = post_id, user=user))

    return render_template('new_comment.html', comment_form=form, posts = post, comments = related_comments, user = user)



@main.route('/post/edit_post/<id>', methods = ['GET','POST'])
@login_required
def edit_post(id):
    form = PostForm()
    post_to_edit = Post.query.get_or_404(id)
    id = current_user.id
    if id == post_to_edit.user.id:

        if form.validate_on_submit():
            post_to_edit.title = form.title.data
            post_to_edit.content = form.content.data
            #post.author = form.author.data
            #update database
            updated_post = Post.save_post(post_to_edit)
            #db.session.add(post)
            #db.session.commit()

            flash("Post has been updated successfully!")

            return redirect(url_for('.new_comment',post = updated_post, post_id = post_to_edit.id))
          
        form.title.data = post_to_edit.title
        form.content.data = post_to_edit.content
        #form.author.data = post.author

        return render_template('edit_post.html', form = form)

    else:
        flash("You are not authorized to edit this post")
        return redirect(url_for('.new_comment',post = post_to_edit, post_id = post_to_edit.id))
    
    

@main.route('/post/delete/<int:id>')
@login_required
def delete_post(id):
    post_to_delete = Post.query.get_or_404(id)
    id = current_user.id
    if id == post_to_delete.user.id:

        try:
            db.session.delete(post_to_delete)
            db.session.commit()

            #return success message
            flash("Blog post has been deleted")
            posts = Post.get_posts()
            posts.reverse()
            quote = get_quote()
            return render_template('index.html', posts = posts, quote=quote)

        except:

            #return error message
            flash("Whoops! The post has not been deleted, try again")
            posts = Post.get_posts()
            posts.reverse()
            return render_template('index.html',  posts = posts, quote=quote)

    else:
        flash("You are not authorized to delete this post")
        posts = Post.get_posts()
        posts.reverse()
        quote = get_quote()
        return render_template('index.html',  posts = posts, quote=quote)

@main.route('/post/comment/delete/<int:id>')
@login_required
def delete_comment(id):
    form = CommentForm()
    comment_to_delete = Comment.query.get_or_404(id)
    post_id = comment_to_delete.post_id
    post = Post.query.get_or_404(post_id)
    id = current_user.id
    if id == comment_to_delete.user_id or id == post.user_id:

        try:
            db.session.delete(comment_to_delete)
            db.session.commit()

            #return success message
            flash("This has been deleted")
            #comments = Comment.get_comments()
            quote = get_quote()
            return render_template('new_comment.html', posts = post, quote=quote, comment_form = form)

        except:

            #return error message
            flash("Whoops! The comment has not been deleted, try again")
            #comments = Comment.get_comments()
            quote = get_quote()
            return render_template('new_comment.html', posts = post, quote=quote, comment_form=form)

    else:
        flash("You are not authorized to delete this comment")
        comments = Comment.get_comments()
        quote = get_quote()
        return render_template('new_comment.html', posts = post, quote=quote , comment_form = form)


