def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError("Negative number of size not allowed")
            return f(*args)
        return wrap
    return validator

# decorator checks if second position index value is non negative
# check_non_negative is not a decorator, but a normal function that
# returns a decorator, python takes create_list and passes it to the
# return value of check_non_negative function which is a decorator,
# closure is also maintained on function argument index of
# outside function


@check_non_negative(1)
def create_list(value, size):
    return [value]*size


print(create_list(5, 3))
print(create_list(-5, 3))
print(create_list(5, -3))
