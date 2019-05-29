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


x = ChineseRT_Natural(5)
y = ChineseRT_Natural(2)
print(x//y)




    