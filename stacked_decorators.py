# Stacked Decorators

def check_user_in_not(username):
    def check_user_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('username') == username:
