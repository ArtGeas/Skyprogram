import pytest
from run import app

KEYS_MUST_HAVE = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_get_json_posts():
    response = app.test_client().get('/api/posts/')
    assert type(response.json) == list
    for dic in response.json:
        assert set(dic.keys()) == KEYS_MUST_HAVE


def test_get_json_post():
    response = app.test_client().get('/api/posts/1/')
    assert type(response.json) == dict
    assert response.json.keys() == KEYS_MUST_HAVE

