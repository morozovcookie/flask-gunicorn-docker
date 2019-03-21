from abc import abstractmethod

from .exceptions import InvalidUsernameValue, InvalidEmailValue, InvalidPasswordValue
from flask_gunicorn_docker.repositories import UserModel


class UserRepository(object):
    @abstractmethod
    def store(self, user: UserModel): pass


class Interactor(object):
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def do(self, user: dict):
        username = user.get('username')
        if username is None or username == '':
            raise InvalidUsernameValue('''username can't be None or empty''')

        email = user.get('email')
        if email is None or email == '':
            raise InvalidEmailValue('''email can't be None or empty''')

        password = user.get('password')
        if password is None or password == '':
            raise InvalidPasswordValue('''password can't be None or empty''')

        user_model = UserModel(
            username=username,
            email=email
        )
        user_model.password = password
        self._repository.store(user=user_model)
