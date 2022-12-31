import pytest
from utils import PostManager


@pytest.fixture()
def post_manager():
    post_manager_instance = PostManager()
    return post_manager_instance


class TestPostManager:

    def test_get_posts_all(self, post_manager):
        posts = post_manager.get_posts_all()
        assert type(posts) == list
        assert len(posts) > 0, 'Нет постов'

    def test_get_posts_by_user(self, post_manager):
        with pytest.raises(ValueError):
            posts = post_manager.get_posts_by_user('zuzu')

    def test_get_comments_by_post_id(self, post_manager):
        with pytest.raises(ValueError):
            comments = post_manager.get_comments_by_post_id(900)

    def test_search_for_posts(self, post_manager):
        posts = post_manager.search_for_posts('кот')
        assert type(posts) == list
        assert len(posts) > 0

    def test_get_post_by_pk(self, post_manager):
        post = post_manager.get_post_by_pk(1)
        assert type(post) == dict
        assert post['pk'] == 1
