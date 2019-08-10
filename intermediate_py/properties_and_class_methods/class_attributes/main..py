class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


sc = ShippingContainer("XML", "text")

sc2 = ShippingContainer("JAVA", ".java")

print(sc)
print(sc.owner_code)
print(sc.contents)
print(sc.serial)

print(sc2)
print(sc2.owner_code)
print(sc2.contents)
print(sc2.serial)

# class attribute can be accessed as following:
print(sc2.next_serial, "using instance variable")
print(ShippingContainer.next_serial, "using class")
