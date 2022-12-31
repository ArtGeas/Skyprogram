from flask import  Blueprint, render_template, jsonify
from utils import PostManager

post_blueprint = Blueprint('post_blueprint', __name__)
post_manager = PostManager()

@post_blueprint.route('/api/posts/')
def get_json_posts():
    posts = post_manager.get_posts_all()
    return jsonify(posts)


@post_blueprint.route('/api/posts/<int:postid>/')
def get_json_post(postid):
    post = post_manager.get_post_by_pk(postid)
    return jsonify(post)


@post_blueprint.route('/posts/<int:postid>/')
def post_page(postid):
    post = post_manager.get_post_by_pk(postid)
    comments = post_manager.get_comments_by_post_id(postid)
    count_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)
