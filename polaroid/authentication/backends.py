from .model import User
from graphql_jwt.backends import JSONWebTokenBackend


def get_user_by_id(user_id):
    User = User
    try:
        return User.objects.get_user_by_id(user_id)
    except USER.DoesNotExist:
        return None

class JSONWebToken(JSONWebTokenBackend):

    def get_user(self, user_id):
        return get_user_by_id(user_id)
