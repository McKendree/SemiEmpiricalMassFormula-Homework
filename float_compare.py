def bad_float_compare(a,b):
    if a == b:
        return True
    else:
        return False

a = 0.1 + 0.1 + 0.1
b = 0.3

assert bad_float_compare(a,b) == True

def good_float_compare(a,b):
    if a - b < 0.0000001 and a - b > -0.0000001:
        return True
    else:
        return False

assert good_float_compare(a,b) == True
