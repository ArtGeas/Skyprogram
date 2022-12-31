import json

PATH_TO_POSTS = 'data/posts.json'
PATH_TO_COMMENTS = 'data/comments.json'


class PostManager:

    def get_posts_all(self):
        """
        Возвращает все посты
        """
        with open(PATH_TO_POSTS, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def get_posts_by_user(self, user_name):
        """
        Возвращает посты пользователя по имени
        """
        user_posts = []
        names_in_posts = []
        posts = self.get_posts_all()
        for post in posts:
            names_in_posts.append(post['poster_name'])
            if user_name == post['poster_name']:
                user_posts.append(post)
        if user_name not in names_in_posts:
            raise ValueError('Такого пользоввателя нет')
        return user_posts

    def get_comments_by_post_id(self, post_id):
        """
        Возвращает комментарии определенного поста
        """
        posts_ids = []
        with open(PATH_TO_COMMENTS, 'r', encoding='utf-8') as file:
            comments = json.load(file)

        post_comments = []
        for comment in comments:
            posts_ids.append(comment['post_id'])
            if post_id == comment['post_id']:
                post_comments.append(comment)
        if post_id not in posts_ids:
            raise ValueError('Такого поста нет')
        return post_comments

    def search_for_posts(self, query):

        """
        Возвращает список постов по ключевому слову
        """
        posts = self.get_posts_all()
        found_posts = []
        for post in posts:
            if query.lower() in post['content'].lower():
                found_posts.append(post)
        return found_posts

    def get_post_by_pk(self, pk):
        """
        Возвращает один пост по его индентификатору
        """
        posts = self.get_posts_all()
        for post in posts:
            if pk == post['pk']:
                return post
