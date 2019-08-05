def escape_unicode(f):
    def wrap(*args, **kwargs):
        string_returned = f(*args, **kwargs)
        print("string returned", string_returned)
        return ascii(string_returned)
    return wrap


@escape_unicode
def french_city():
    return "Orléans"

# escape_unicode takes french_city as parameter, returns wrap, when we called ()
# after french city, its escape_unicode(), here wrap gets called,
# wrap doesn't have *args, **kwargs since french_coty doesn't have any
# it triggers french_city takes result
# returns ascii of the result.

print(french_city())
