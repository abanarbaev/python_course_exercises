from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #1. Code to execute BFEORE calling the decorated function.
        #2. Вызов декорируемой функции и возврат
        #   полученных от нее результатовю
        return func(*args, **kwargs)

        #3. Код для выполнения ВМЕСТО вызова декорируемой функции.
    return wrapper


"""
from flask import session
from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
"""
