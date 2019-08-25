import iso6346


class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    # to define a class method, decorate
    # method with @classmethod,
    # the argument to the method is cls
    # since class keyword cannot be used.
    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    """
        When to use static method vs static method:
        Rule:
            If we need to use the class object within the class
            use classmethod. If such requirement is not there, use
            staticmethod, static methods have a leading underscore,
            they are not accessible from class object or instance object.
    """

    # cls is same as using ShippingContainer.
    # here class method is used for a named constructor.
    # below method creates an empty shipping container
    # with contents as None.
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(owner_code=owner_code,
                                       serial=ShippingContainer._get_next_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category='R')


"""
Usage:
>>> from main import ShippingContainer
>>> s=ShippingContainer("fru", "Orange")
>>> s.bic
'fruU0013370'
>>> from main import RefrigeratedShippingContainer
>>> r = RefrigeratedShippingContainer("veg", "Lettuce")
>>> r.bic
'vegR0013380'
"""
