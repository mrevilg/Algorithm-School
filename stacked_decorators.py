# Stacked Decorators

def check_user_in_not(username):
    def check_user_decorator(f):