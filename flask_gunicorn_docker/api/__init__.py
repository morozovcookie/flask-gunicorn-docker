from flask import Blueprint


_url_prefix = '/api/v1'

users_api_bp = Blueprint(
    name='user_api',
    import_name=__name__,
    url_prefix='{url_prefix}/users'.format(url_prefix=_url_prefix)
)
