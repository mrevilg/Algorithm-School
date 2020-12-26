# Creating decorators in Python

def identify(f):
    return f

@identify
def foo():
    return 'bar'

# ... is the same as writing:

def foo():
    return 'bar'
    
foo = identify(foo)


# ... Creating decorators

class Store(object):