import functools

# functools.wraps takes function that is getting decorated
# and preserves the documentation, name and other metadata


def nooperation_without(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        return f(*args, **kwargs)
    return wrap


@nooperation_without
def hello():
    "prints hello world"
    print("hello, world")


print('--------------')
hello()
print("***name")
print(hello.__name__)
print("***doc")
print(hello.__doc__)
print("***help")
print(help(hello))
