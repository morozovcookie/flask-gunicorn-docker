from abc import abstractmethod
from typing import List

from flask_gunicorn_docker.model import User


class UsersList(object):
    class UserRepository(object):
        @abstractmethod
        def list(self, limit: int, offset: int) -> List[User]: pass

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def do(self, limit: int, offset: int) -> List[dict]:
        users = self._repository.list(limit=limit, offset=offset)

        return [{
            'id':       user.id,
            'username': user.username,
            'email':    user.email
        } for user in users]


class StoreUser(object):
    class UserRepository(object):
        @abstractmethod
        def store(self, user: User): pass

    def __init__(self, repository: UserRepository):
        self._repository = repository

    def do(self, user: dict):
        username = user.get('username')
        if username is None or username == '':
            raise Exception('''username can't be None or empty''')

        email = user.get('email')
        if email is None or email == '':
            raise Exception('''email can't be None or empty''')

        password = user.get('password')
        if password is None or password == '':
            raise Exception('''password can't be None or empty''')

        user_model = User(
            username=username,
            email=email
        )
        user_model.password = password
        self._repository.store(user)
