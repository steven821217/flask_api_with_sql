# from werkzeug.security import safe_str_cmp # for python 2.7
# from werkzeug.security import safe_str_cmp # for python 2.7
from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password:
    # if user and safe_str_cmp(user.password, password): # for python 2.7
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)