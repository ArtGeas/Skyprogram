from flask import Blueprint, render_template, redirect
from utils import PostManager
import json

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__)
post_manager = PostManager()


@bookmarks_blueprint.route('/bookmarks/')
def bookmarks_page():
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = json.load(file)

    return render_template('bookmarks.html', bookmarks=bookmarks)


@bookmarks_blueprint.route('/bookmarks/add/<int:postid>/')
def add_bookmark_page(postid):
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        posts_check = json.load(file)

    for post_check in posts_check:
        if postid == post_check['pk']:
            return redirect('/', code=302)

    post = post_manager.get_post_by_pk(postid)
    posts_check.append(post)

    with open('data/bookmarks.json', 'w') as file:
        json.dump(posts_check, file)

    return redirect('/', code=302)

@bookmarks_blueprint.route('/bookmarks/del/<int:postid>/')
def del_bookmark_page(postid):
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        posts_check = json.load(file)

    for post_check in posts_check:
        if postid == post_check['pk']:
            posts_check.remove(post_check)

    with open('data/bookmarks.json', 'w') as file:
        json.dump(posts_check, file)

        return redirect('/bookmarks/', code=302)

