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


# Main constants
primes = (97, 101, 103, 107, 109, 113, 127, 131)
m = 1
for i in range(len(primes)):
    m *= primes[i]
mi = tuple([m // primes[i] for i in range(len(primes))])
miopp = tuple([inverse_el(mi[i], primes[i]) for i in range(len(primes))])

# For comparsion 1
Sq = sum(mi)
si = [( -inverse_el(primes[i], Sq)) % Sq  for i in range(len(primes))]


class RNS_Natural:
    def __init__(self, arg):
        self.primes = primes
        self.m = m
        self.mi = mi
        self.miopp = miopp
        self.x = -1
        self.d = -1
        self._compare_mod = 2
        
        if type(arg) == type(list()) and len(arg) == len(self.primes):
            self.r = tuple([arg[i] for i in range(len(primes))].copy())
        elif type(arg) == type(tuple()) and len(arg) == len(self.primes):
            self.r = tuple([arg[i] for i in range(len(primes))].copy())
        elif type(arg) == type(int()) or type(arg) == type(str()):
            arg = int(arg)
            assert arg >= 0
            self.r = [0 for i in range(len(self.primes))]
            for i in range(len(self.primes)):
                self.r[i] = arg % self.primes[i]
            self.x = arg
        elif type(arg) == type(RNS_Integer(1)):
            assert arg.b == 0
            self.r = arg.r
        elif type(arg) == type(RNS_Natural(1)):
            pass
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
        
    
    def __str__(self):
        return ("RNS_Natural(" + str(self.value()) + ")")    
        
        
    def __eq__(self, other):
        assert type(self) == type(other)
        res = True
        i = 0
        while res and i < len(self.primes):
            res = res and self.r[i] == other.r[i]
            i += 1
        return res
    
    
    def __ne__(self, other):
        assert type(self) == type(other)
        return not(self == other)
    
    
    def __add__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = (self.r[i] + other.r[i]) % self.primes[i]
        z = RNS_Natural(res)
        assert z >= self and z >= other
        return z
    
    
    def __sub__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = (self.r[i] - other.r[i]) % self.primes[i]
        z = RNS_Natural(res)
        assert z <= self
        return z
    
    
    def __mul__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = (self.r[i] * other.r[i]) % self.primes[i]
        z = RNS_Natural(res)
        assert z >= self and z >= other
        return z
    
    
    # 1 / self
    def inverse(self):
        res = [0 for i in range(len(self.primes))]
        for i in range(len(self.primes)):
            res[i] = inverse_el(self.r[i], self.primes[i])
        return RNS_Natural(res)
    
    
    def __truediv__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        inv = other.inverse()
        for i in range(len(self.primes)):
            res[i] = (self.r[i] * inv.r[i]) % self.primes[i]
        return RNS_Natural(res)
        
    
    # For comparsion #TODO
    def _d_function(self):
        return (sum([si[i]*self.r[i] \
                     for i in range(len(primes))])) % Sq
    
    def _compare(self, other):
        assert type(self) == type(other)
        if self.d == -1:
            self.d = self._d_function()
        if other.d == -1:
            other.d = other._d_function()
            
        if self.d > other.d:
            return 2
        elif self.d < other.d:
            return 1
        else:
            if self.r[0] > other.r[0]:
                return 2
            elif self.r[0] < other.r[0]:
                return 1
            else:
                return 0
            
            
    def __lt__(self, other):
        assert type(self) == type(other)
        c = self._compare(other)
        return c == 1
        
        
    def __le__(self, other):
        assert type(self) == type(other)
        c = self._compare(other)
        return c == 1 or c == 0
    
    
    def __gt__(self, other):
        assert type(self) == type(other)
        c = self._compare(other)
        return c == 2
    
    
    def __ge__(self, other):
        assert type(self) == type(other)
        c = self._compare(other)
        return c == 2 or c == 0        
            
    
    def _divide(self, other):
        assert type(self) == type(other) and other != RNS_Natural(0)
        x, y = self, other
        
        q = RNS_Natural(0)
        e = RNS_Natural(1)
        r = x
        while r >= y:
            q += e
            r -= y
        return q, r
    
    
    def __floordiv__(self, other):
        assert type(self) == type(other) and other != RNS_Natural(0)
        return self._divide(other)[0]
        
        
    def __mod__(self, other):
        assert type(self) == type(other) and other != RNS_Natural(0)
        return self._divide(other)[1]
    

class RNS_Integer(RNS_Natural):
    def __init__(self, arg):
        if type(arg) == type(list()) and len(arg) == len(self.primes):
            self.b = 0
        elif type(arg) == type(tuple()) and len(arg) == len(self.primes):
            self.b = 0
        elif type(arg) == type(int()) or type(arg) == type(str()):
            arg = int(arg)
            self.b = int(arg < 0)
            arg = abs(arg)
        elif type(arg) == type(RNS_Natural()) or type(arg) == type(RNS_Integer):
            pass
        else:
            raise TypeError
        
        super().__init__(arg)
    
    
    def __neg__(self):
        res = RNS_Integer()
        res.b = int(not(bool(self.b)))
        return res
    
    
    def __str__(self):
        b = ""
        if self.b:
            b = "-"
        return ("RNS_Integer(" + b + str(self.value()) + ")")  
    
    
    def __eq__(self, other):
        if self.b == other.b:
            return super().__eq__(self, other)
        else:
            return False
    
    def __abs__(self):
        return RNS_Integer(self.r)
    
    
    def __add__(self, other):
        assert type(self) == type(other)
        if self.b == other.b:
            res = RNS_Integer(super().__add__(self, other))
            res.b = other.b
        else:
            if abs(self) == abs(other):
                res = RNS_Integer(0)
            elif abs(self) > abs(other):
                res = self - other
                res.b = self.b
            else:
                res = other - self
                res.b = other.b
        return res
    
    
    def __sub__(self, other):
        assert type(self) == type(other)
        return self + (-other)
    
    
    def __mul__(self, other):
        assert type(self) == type(other)
        res = RNS_Integer(super().__mul__(self, other))
        if self.b == other.b:
            res.b = 0
        else:
            res.b = 1
        return res
    
    def __floordiv__(self, other):
        assert type(self) == type(other) and other != RNS_Integer(0)
        res = RNS_Integer(super().__floordiv__(self, other))      
        if self.b == other.b:
            res.b = 0
        else:
            res.b = 1      
        return res
    
    def __mod__(self, other):
        assert type(self) == type(other) and other != RNS_Integer(0)
        res = RNS_Integer(super().__mod__(self, other))      
        if self.b == other.b:
            res.b = 0
        else:
            res.b = 1      
        return res