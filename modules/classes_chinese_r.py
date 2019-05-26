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
Sq = sum(primes)
si = [( -inverse_el(mi[i], Sq)) % Sq  for i in range(len(primes))]


class ChineseRT_Natural:
    def __init__(self, arg):
        self.primes = primes
        self.m = m
        self.mi = mi
        self.miopp = miopp
        self.x = -1
        self.d = -1
        self._compare_mod = 1
        
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
        
    
    def __str__(self):
        return ("ChineseRT_Natural(" + str(self.value()) + ")")    
        
        
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
    
    
    def __truediv__(self, other):
        assert type(self) == type(other)
        res = [0 for i in range(len(self.primes))]
        inv = other.inverse()
        for i in range(len(self.primes)):
            res[i] = (self.r[i] * inv.r[i]) % self.primes[i]
        return ChineseRT_Natural(res)
        
    
    # For comparsion 1
    def _d_function(self):
        return (sum([si[i]*self.r[i] \
                     for i in range(len(primes))])) % Sq
    
    # Comparsion 1
    def _compare1(self, other):
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
       
    
    def _compare(self, other):
        if self._compare_mod == 1:
            return self._compare1(other)
            
            
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
        assert type(self) == type(other)
        x, y = self, other
        
        result = 0
        while x >= y:
            result += 1
            x -= y
        
        return ChineseRT_Natural(result), x
    
    
    def __floordiv__(self, other):
        assert type(self) == type(other)
        return self._divide(other)[0]
        
        
    def __mod__(self, other):
        assert type(self) == type(other)
        return self._divide(other)[1]
        