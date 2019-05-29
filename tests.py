from modules.classes_RNS import *
from modules.classes import *
from modules.N import *
from random import randrange

from time import clock


def gcd_rns(x, y):
    z = RNS_Natural(0)
    
    while x != z and y != z:
        if x > y:
            x = x % y
        else:
            y = y % x
    
    return x + y


def lcm_rns(x, y):
    return x*y//gcd_rns(x, y)


for i in range(100000000000, 10000000000001, 100000000000):
    x1 = RNS_Natural(i)
    y1 = RNS_Natural(i+1)
    x2 = Natural()
    x2.read_from_str(str(i))
    y2 = Natural()
    y2.read_from_str(str(i+1))
    print("Cur task: comp("+str(i)+", 23)")
    
    print("RNS "+str(i//10000))
    p_time = clock()
    x1 > y1
    print(str((clock() - p_time)*10**6))
    
    print("Traditional "+str(i//10000))
    p_time = clock()
    COM_NN_D(x2, y2)
    print(str((clock() - p_time)*10**6), end="\n\n")
    