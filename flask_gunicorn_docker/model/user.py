from flask_gunicorn_docker import db, flask_bcrypt


class User(db.Model):
    """
        User Model for storing user related details
    """

    __tablename__ = "users"

    id = db.Column(name="id", type_=db.BigInteger, autoincrement=True, primary_key=True)
    username = db.Column(name="username", type_=db.String(255), nullable=False, unique=True)
    email = db.Column(name="email", type_=db.String(255), nullable=False)
    password_hash = db.Column(name="password", type_=db.String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
