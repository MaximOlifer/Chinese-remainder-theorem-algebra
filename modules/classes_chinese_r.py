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
mi = tuple([int(m/primes[i]) for i in range(len(primes))])
miopp = tuple([inverse_el(mi[i], primes[i]) for i in range(len(primes))])


class ChineseRT_Natural:
    def __init__(self, arg):
        self.primes = primes
        self.m = m
        self.mi = mi
        self.miopp = miopp
        
        if type(arg) == type(list()):
            self.r = arg.copy()
        elif type(arg) == type(int()):
            self.r = [0 for i in range(len(self.primes))]
            for i in range(len(self.primes)):
                self.r[i] = arg % self.primes[i]
        self.r = tuple(self.r)
        
        self.x = -1
    
    
    def value(self):
        if self.x != -1:
            return self.x
        else:
            self.x = 0
            for i in range(len(self.primes)):
                self.x += self.r[i]*self.mi[i]*self.miopp[i]
            self.x %= self.m
            return self.x
    
    
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
    
    
    def inverse(self):
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = inverse_el(self.r[i], self.primes[i])
        return ChineseRT_Natural(res) 
        
    
    """
    def __div__(self, other):
        assert type(self) == type(other)
        res = ChineseRT_Natural(0)
        for i in range(len(self.primes)):
            res.r[i] = (self.r[i] * other.r[i]) % self.primes[i]
        return res
    """
    
    """
    def __mod__(self, other):
        assert type(self) == type(other)
        res = ChineseRT_Natural(0)
        for i in range(len(self.primes)):
            res.r[i] = (self.r[i] * other.r[i]) % self.primes[i]
        return res
    """    
    