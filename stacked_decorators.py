# Stacked Decorators

def check_user_in_not(username):
    def check_user_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('username') == username:
                raise Exception("This user is not allowd to get food")
            return f(*args, **kwargs)
        return wrapper
    return check_user_decorator

class Store(object):
    @check_user_in_not("admin")
    @check_user_in_not("user123")
