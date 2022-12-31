from flask import Blueprint, render_template, request
from utils import PostManager
import json
import logging

main_blueprint = Blueprint('main_blueprint', __name__)
post_manager = PostManager()


@main_blueprint.route('/')
def main_page():
    posts = post_manager.get_posts_all()
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        bookmarks = len(json.load(file))
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@main_blueprint.route('/search/')
def search_page():
    s = request.args.get('s')
    found_posts = post_manager.search_for_posts(s)
    first_10_posts = found_posts[0:10]
    posts_number = len(found_posts)
    return render_template('search.html', posts=first_10_posts, posts_number=posts_number)
