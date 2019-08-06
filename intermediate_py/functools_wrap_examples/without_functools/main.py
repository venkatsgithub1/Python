def nooperation_without(f):
    def wrap(*args, **kwargs):
        if(kwargs['replace_dunders'] == True):
            wrap.__name__ = f.__name__
            wrap.__doc__ = f.__doc__
        return f(*args, **kwargs)
    return wrap


@nooperation_without
def hello(replace_dunders=False):
    "prints hello world"
    print("hello, world")


print('--------------')
print("after calling hello with replace_dunders=False")
hello(replace_dunders=False)
print("***name")
print(hello.__name__)
print("***doc")
print(hello.__doc__)
print("***help")
print(help(hello))

print('--------------')
hello(replace_dunders=True)
print("after calling hello with replace_dunders=True")
print("***name")
print(hello.__name__)
print("***doc")
print(hello.__doc__)
print("***help")
print(help(hello))
