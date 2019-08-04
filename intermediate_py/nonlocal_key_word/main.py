import time

# Outer method that has a variable called last_called,
# the variable is used by inner function.
def make_timer():
    last_called = None

    # method references last_called nonlocal
    # variable
    # elapsed function has reference to last_called
    # state of the variable is held by the method.
    # whenever we call elapsed again and again
    # by make_timer, it uses last state of
    # last_called variable and calculates
    # time.
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called=now
            return None
        time_lapsed = now - last_called
        lasat_called = now
        return time_lapsed
    return elapsed

# usage: go to the folder in which py file is present and open python 
# in terminal, import method make_timer from file and run inner method
# again and again.