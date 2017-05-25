class Animal (object):
    def __init__ (self, name):
        self.name=name

# "Jeffrey" becomes name.
# zebra gets Animal instance and can access name.

zebra=Animal ("Jeffrey")

print (zebra.name)
