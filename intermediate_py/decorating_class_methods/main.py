def escape_unicode(f):
    def wrap(*args, **kwargs):
        res=f(*args, **kwargs)
        return ascii(res)
    return wrap

class Tracer:
    def __init__(self):
        self.enabled=True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Tracer()

@tracer
@escape_unicode
def french_city():
    return "Orléans"

class Island_Maker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix

# decorating class method is like decorating a normal method

"""
Usage:
>>> from main import Island_Maker
>>> is_ma = Island_Maker('Island')
>>> is_ma.make_island('Python')
calling <function Island_Maker.make_island at 0x7ff59051f488>
'PythonIsland'
>>> is_ma.make_island('Django')
calling <function Island_Maker.make_island at 0x7ff59051f488>
'DjangoIsland'
>>> from main import tracer
>>> tracer.enabled=False
>>> is_ma.make_island('BeautifulSoup')
'BeautifulSoupIsland'
"""