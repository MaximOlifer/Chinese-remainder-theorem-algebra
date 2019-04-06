def bezout(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)


def inverse_el(x, m):
    return int(bezout(x, m)[0]) % m


primes = (97, 101, 103, 107, 109, 113, 127, 131)
m = 1
for i in range(len(primes)):
    m *= primes[i]
mi = tuple([m // primes[i] for i in range(len(primes))])
miopp = tuple([inverse_el(mi[i], primes[i]) for i in range(len(primes))])


class ChineseRT_Natural:
    def __init__(self, arg):
        self.primes = primes
        self.m = m
        self.mi = mi
        self.miopp = miopp
        self.x = -1
        
        if type(arg) == type(list()) and len(arg) == len(self.primes):
            self.r = arg.copy()
        elif type(arg) == type(tuple()) and len(arg) == len(self.primes):
            self.r = arg
        elif type(arg) == type(int()):
            self.r = [0 for i in range(len(self.primes))]
            for i in range(len(self.primes)):
                self.r[i] = arg % self.primes[i]
            self.x = arg
        else:
            raise TypeError
        
        self.r = tuple(self.r)
    
    
    def value(self):
        # TODO 
        # необходимо переделать вычисления здесь
        # c использованием своих алгоритмов
        if self.x != -1:
            return self.x
        else:
            self.x = 0
            for i in range(len(self.primes)):
                self.x += self.r[i]*self.mi[i]*self.miopp[i]
            self.x %= self.m
            return self.x
        
        
    def __eq__(self, other):
        assert type(self) == type(other)
        res = True
        i = 0
        while res and i < len(self.primes):
            res = res and self.r[i] == other.r[i]
            i += 1
        return res
    
    
    def __add__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = (self.r[i] + other.r[i]) % self.primes[i]
        return ChineseRT_Natural(res)
    
    
    def __sub__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = (self.r[i] - other.r[i]) % self.primes[i]
        return ChineseRT_Natural(res)
    
    
    def __mul__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = (self.r[i] * other.r[i]) % self.primes[i]
        return ChineseRT_Natural(res)
    
    
    # 1 / self
    def inverse(self):
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = inverse_el(self.r[i], self.primes[i])
        return ChineseRT_Natural(res)
        
        
    """
    def __floordiv__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        zero = ChineseRT_Natural(0)
        for i in range(len(self.primes)):
            res[i] = (self.r[i] - other.r[i]) % self.primes[i]
        return ChineseRT_Natural(res)
    """
    
    
    def __truediv__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        inv = other.inverse()
        for i in range(len(self.primes)):
            res[i] = (self.r[i] * inv.r[i]) % self.primes[i]
        return ChineseRT_Natural(res)
        
    
    """
    def __mod__(self, other):
        assert type(self) == type(other)
        return self - other*(self // other)
    """
    