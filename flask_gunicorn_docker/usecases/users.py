from abc import abstractmethod
from typing import List

from flask_gunicorn_docker.model import User


class UsersList(object):
    class UserRepository(object):
        @abstractmethod
        def list(self, limit: int, offset: int) -> List[User]: pass

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def do(self, limit: int, offset: int):
        users = self.repository.list(limit=limit, offset=offset)

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
        self.repository = repository

    def do(self, user: dict):
        pass
