# I

'''
    Understanding GCD:
    gcd (48, 7) => |
    48 = 7 * 6 + 6 | a = 48, b = 7, m = a // b, r = a%b
    7 = 6 * 1 + 1  | a = b, b = r , m =
    1 = 1 * 1 + 0
'''

def gcd(a, b):
    # Set the variables in equation to be equal: a = b * m + r
    m = a//b
    r = a%b

    while r > 0:
        a = b
        b = r
        m = a//b
        r = a%b

