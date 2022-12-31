from flask import Blueprint, render_template
from utils import PostManager

users_blueprint = Blueprint('users_blueprint', __name__)
post_manager = PostManager()


@users_blueprint.route('/users/<username>')
def user_page(username):
    user_posts = post_manager.get_posts_by_user(username)
    posts_name = username
    return render_template('user-feed.html', posts=user_posts, posts_name=posts_name)
