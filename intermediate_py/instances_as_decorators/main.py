class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wrap


# creating an instance of the class
tracer = Trace()

# instance becomes decorator now
# when method is called, a trigger to
# instance's __call__ is issued
# dunder call returns a function, uncalled
# call on rotate_list calls
# return function returned by dunder call
@tracer
def rotate_list(list_to_rotate):
    return list_to_rotate[1:]+[list_to_rotate[0]]

"""
Usage:
>>> from main import tracer, rotate_list
>>> list_1=[2,4,6,8]
>>> list_1=rotate_list(list_1)
Calling <function rotate_list at 0x7f92d1593950>
>>> list_1
[4, 6, 8, 2]
>>> list_1=rotate_list(list_1)
Calling <function rotate_list at 0x7f92d1593950>
>>> list_1
[6, 8, 2, 4]
>>> # disabling tracer
...
>>> tracer.enabled = False
>>> list_1=rotate_list(list_1)
>>> list_1
[8, 2, 4, 6]
"""