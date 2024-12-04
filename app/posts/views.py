from . import post_bp
from flask import render_template, request, abort, flash, redirect, url_for
from .forms import PostForm
from .models import Post
from app import db


@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        author = form.author.data
        is_active = form.is_active.data
        publish_date = form.publish_date.data

        post_new = Post(
            title=title,
            content=content,
            category=category,
            author=author,
            is_active=is_active,
            posted=publish_date
        )

        db.session.add(post_new)
        db.session.commit()

        flash(f'Post "{title}" added successfully!', 'success')

        return redirect(url_for('.get_posts'))

    elif form.errors:
        flash(f"Enter the correct data in the form!", "danger")

    return render_template("add_post.html", form=form)

@post_bp.route('/delete_post/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get(id)

    if post:
        db.session.delete(post)
        db.session.commit()

        flash(f'Post "{post.title}" deleted successfully!', 'success')
    else:

        flash('Post not found!', 'danger')

    return redirect(url_for('posts.get_posts'))



@post_bp.route('/')
def get_posts():
    stmt = db.select(Post).order_by(
        Post.posted.desc())
    posts = db.session.scalars(stmt).all()
    return render_template("posts.html", posts=posts)


@post_bp.route('/<int:id>')
def detail_post(id):
    post = Post.query.get(id)
    if post:
        return render_template('detail_post.html', post=post)
    return abort(404)


@post_bp.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get(id)
    if not post:
        flash('Post not found!', 'danger')
        return redirect(url_for('.get_posts'))

    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.author = form.author.data
        post.is_active = form.is_active.data
        post.posted = form.publish_date.data

        db.session.commit()

        flash(f'Post "{post.title}" updated successfully!', 'success')

        return redirect(url_for('.detail_post', id=post.id))

    return render_template('edit_post.html', form=form, post=post)