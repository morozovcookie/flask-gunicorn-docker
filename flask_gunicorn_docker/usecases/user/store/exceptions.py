from flask_gunicorn_docker import FlaskUnicornDockerBaseException


class InvalidUsernameValue(FlaskUnicornDockerBaseException):
    """
        Exception will be raised when username is empty or is None
    """


class InvalidEmailValue(FlaskUnicornDockerBaseException):
    """
        Exception will be raised when email is empty or is None
    """


class InvalidPasswordValue(FlaskUnicornDockerBaseException):
    """
        Exception will be raised when password is empty or is None
    """
