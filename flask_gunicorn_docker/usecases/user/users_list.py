from abc import abstractmethod
from typing import List

from flask_gunicorn_docker.repositories import UserModel


class UserRepository(object):
    @abstractmethod
    def list(self, limit: int, offset: int) -> List[UserModel]: pass


class UsersList(object):
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def do(self, limit: int, offset: int) -> List[dict]:
        users = self._repository.list(limit=limit, offset=offset)

        return [{
            'id':       user.id,
            'username': user.username,
            'email':    user.email
        } for user in users]
