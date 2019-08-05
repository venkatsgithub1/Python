class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("calling {}".format(f))
            return f(*args, **kwargs)
        return wrap


def escape_unicode(f):
    def wrap(*args, **kwargs):
        res = f(*args, **kwargs)
        return ascii(res)
    return wrap

tracer=Trace()

# first the name is passed to escape_unicode, which returns wrap
# the wrap's result is passed to tracer's dunder call and 
# the wrap of dunder call is finally called.
@tracer
@escape_unicode
def french_city(name):
    return name

"""
Usage:
>>> from main import tracer, french_city
>>> french_city('Étretat')
calling <function escape_unicode.<locals>.wrap at 0x7f7755486268>
"'\\xc9tretat'"
>>> tracer.enabled=False
>>> french_city('Nîmes')
"'N\\xeemes'"
"""