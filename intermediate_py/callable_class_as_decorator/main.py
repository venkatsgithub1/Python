class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('hello, {}'.format(name))

# Usage: open terminal, open python console
# import class and method from file
# call instance variable as method again
# after calling few times, check
# count variable
# dunder call method makes the class instance callable
# it will allow class be a decorator
"""
>>> from main import CallCount, hello
>>> c1=CallCount(hello)
>>> c1('py')
hello, py
>>> c1('django')
hello, django
>>> c1.count
2
"""