class ChineseRT_Natural:
    def __init__(self, r1=0, r2=0, r3=0, r4=0, r5=0, r6=0, r7=0, r8=0):
        self.primes = [97, 101, 103, 107, 109, 113, 127, 131]
        self.m = 1
        for i in range(len(self.primes)):
            self.m *= self.primes[i]
        self.mi = [int(self.m/self.primes[i]) for i in range(len(self.primes))]
        self.miopp = [int(self.bezout(self.mi[i], self.primes[i])[0]) % self.primes[i] for i in range(len(self.primes))]
        self.r = [r1, r2, r3, r4, r5, r6, r7, r8]
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
        res = ChineseRT_Natural()
        for i in range(len(self.primes)):
            res.r[i] = (self.r[i] + other.r[i]) % self.primes[i]
        return res
    
    
    def __sub__(self, other):
        assert type(self) == type(other)
        res = ChineseRT_Natural()
        for i in range(len(self.primes)):
            res.r[i] = (self.r[i] - other.r[i]) % self.primes[i]
        return res
    
    
    def __mul__(self, other):
        assert type(self) == type(other)
        res = ChineseRT_Natural()
        for i in range(len(self.primes)):
            res.r[i] = (self.r[i] * other.r[i]) % self.primes[i]
        return res     
    
    
    def bezout(self, a, b):
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
    
        
        