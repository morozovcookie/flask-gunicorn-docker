from abc import abstractmethod


class UsersList(object):
    class UserRepository(object):
        @abstractmethod
        def list(self): pass

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def do(self):
        users = self.repository.list()
        if users is None:
            return []

        return []


class StoreUser(object):
    class UserRepository(object):
        @abstractmethod
        def store(self): pass

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def do(self, user):
        pass
