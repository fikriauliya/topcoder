def gcd(a,b):
    (b,a) = sorted( (a,b) )
    while b != 0:
        (a,b) = (b, a%b)
    return a

def lcm(a,b):
    return a*b / gcd(a,b)
