from flask_gunicorn_docker import Base, flask_bcrypt
from sqlalchemy import Column, BigInteger, String


class Model(Base):
    """
        Model for storing user related details
    """

    __tablename__ = "users"

    id = Column(name="id", type_=BigInteger, autoincrement=True, primary_key=True)
    username = Column(name="username", type_=String(255), nullable=False, unique=True)
    email = Column(name="email", type_=String(255), nullable=False, unique=True)
    password_hash = Column(name="password", type_=String(255), nullable=False)

    def __init__(self, username: str, email: str, id: int = 0):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = None

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password: str):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
