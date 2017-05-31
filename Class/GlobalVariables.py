class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health="good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description (self):
        print (self.name)
        print (self.age)
        print (self.health)
        
hippo=Animal ("Bobby",1)
sloth=Animal ("Lazy",2)
ocelot=Animal ("Shorty",3)
hippo.description()
sloth.description()
ocelot.description()
