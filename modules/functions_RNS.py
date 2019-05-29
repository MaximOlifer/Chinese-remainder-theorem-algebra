def gcd_rns(x, y):
    z = ChineseRT_Natural(0)
    
    while x != z and y != z:
        if x > y:
            x = x % y
        else:
            y = y % x
    
    return x + y


def lcm_rns(x, y):
    return x*y//gcd_rns(x, y)

