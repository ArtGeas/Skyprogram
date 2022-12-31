from flask import Flask
from main.views import main_blueprint
from post.views import post_blueprint
from users.views import users_blueprint
from tags.views import tags_blueprint
from bookmarks.views import bookmarks_blueprint
import logging


logging.basicConfig(filename='logs/api.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s',
                    encoding='utf-8')

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(bookmarks_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404


@app.errorhandler(500)
def internal_server_error(e):
    return 'Internal Server Error', 500


if __name__ == '__main__':
    app.run()
