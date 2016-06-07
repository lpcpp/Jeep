from admin.models import User
from common.utils import md5


def get_user_by_username(username):
    try:
        user = User.objects.get(username=username)
    except:
        return None

    return user


def create_user(username, password):
    user = User(username=username, password=md5(password))
    user.save()
