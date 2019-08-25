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
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(owner_code=owner_code,
                                                       serial=ShippingContainer._get_next_serial())

class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
"""
Usage:
>>> from main import *
>>> r = RefrigeratedShippingContainer.create_with_items("fru", ["Grapes", "Apple"], celsius=3.0)
>>> r
<main.RefrigeratedShippingContainer object at 0x7f143e34ac50>
"""