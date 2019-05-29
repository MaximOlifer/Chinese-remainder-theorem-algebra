import classes_chinese_r
from classes_chinese_r import *
from classes import *
from random import randrange
from time import clock


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

x = ChineseRT_Natural(6)
y = ChineseRT_Natural(2)
print(x.r)
print(y.r)
print(y.inverse().r)
z = x / y
print(z.r)
print(z.value())




    