# Remove String Spaces
import signal


def no_space(x):
    new_str = " "
    for i in x:
        if i != " ":
            new_str += i 
    return new_str
print(no_space("Sir Tava Nabichvari"))
