def create_multipliers():
    return [lambda x : i * x for i in range(5)]


def create_multipliers_equivalent():
    multipliers = []

    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)

    return multipliers

# Python’s closures are late binding. This means that the values of variables used in closures are looked up
# at the time the inner function is called.
# Here, whenever any of the returned functions are called, the value of i is looked up in the surrounding scope
# at call time. By then, the loop has completed and i is left with its final value of 4.
# This prints, 8, 8 ,8 ,8 , 8
for multiplier in create_multipliers():
    print multiplier(2)


# fix: use default argument which is created at the time the function is defined
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]