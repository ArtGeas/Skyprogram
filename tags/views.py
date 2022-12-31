from flask import Blueprint, render_template
from utils import PostManager

tags_blueprint = Blueprint('tags_blueprint', __name__)
post_manager = PostManager()


@tags_blueprint.route('/tag/<tagname>')
def tag_page(tagname):
    posts = post_manager.get_posts_all()
    tag_posts = []
    full_tag = '#' + tagname
    for post in posts:
        if full_tag in post['content']:
            tag_posts.append(post)
    return render_template('tag.html', posts=tag_posts, tagname=tagname.upper())
