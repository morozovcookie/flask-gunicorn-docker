from abc import abstractmethod
from typing import List

from .model import Model


class Storage(object):
    @abstractmethod
    def execute_on_slave(self, clause, params=None, mapper=None, bind=None, **kw): pass

    @abstractmethod
    def execute_on_master(self, clause, params=None, mapper=None, bind=None, **kw): pass


class Repository(object):
    def __init__(self, storage: Storage):
        self._storage = storage

    def list(self, limit: int, offset: int) -> List[Model]:
        query = '''SELECT id,
                          username,
                          email
                   FROM users
                   LIMIT :limit
                   OFFSET :offset'''

        rows = self._storage.execute_on_slave(
            clause=query,
            params={
                'limit':  limit,
                'offset': offset
            }
        ).fetchall()
        if rows is None:
            return []

        return [Model(id=row['id'],
                      username=row['username'],
                      email=row['email']
                      ) for row in rows]

    def store(self, user: Model):
        query = '''INSERT INTO users 
                        (username, email, password) 
                   VALUES
                        (:username, :email, :password_hash)'''

        self._storage.execute_on_master(
            clause=query,
            params={
                'username':      user.username,
                'email':         user.email,
                'password_hash': user.password_hash,
            }
        )
