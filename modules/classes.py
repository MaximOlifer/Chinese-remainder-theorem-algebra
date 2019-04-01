class Natural (list):
    def __init__ (self, n = 0, a1=0, *args):
        self.n = n
        args = list(args)
        args.insert(0, a1)
        super().__init__(args)
    
    
    def copy(self):
        return Natural(self.n, *super().copy())
        
    
    # Перевод в строку
    def __str__(self):
        num = self.copy()
        num.reverse()
        string = ''
        for i in range(num.n+1):
            string += str(num[i])
        return string
    
    
    # Обновление из строки
    def read_from_str(self, string):
        self.clear()
        self.n = 0
        for c in string:
            self.append(int(c))
            self.n += 1
        self.reverse()
        self.n -= 1
        

class Integer(Natural):
    def __init__(self, b = 0, n = 0, a1=0, *args):
        self.b = b
        args = list(args)
        super().__init__(n, a1, *args)
    
    
    def copy(self):
        return Integer(self.b, self.n, *super().copy())
    
    
    def __str__(self):
        string = super().__str__()
        if self.b == 1:
            string = '-' + string
        else:
            string = '+' + string
        return string
    
    
    def read_from_str(self, string):
        if string[0] == '-':
            if string != '-0':
                self.b = 1
            string = string[1::]
        elif string[0] == '+':
            string = string[1::]
            self.b = 0
        else:
            self.b = 0
        super().read_from_str(string)


class Rational:
    def __init__(self, m = Integer(), n = Natural(0, 1)):
        self.m = m.copy()
        self.n = n.copy()
    
    
    def copy(self):
        return Rational(self.m.copy(), self.n.copy())
    
    
    def __str__(self):
        # Если числитель 0
        if self.m.n == 0 and self.m[0] == 0:
            string = '0'
        # Если знаменатель 1
        elif self.n.n == 0 and self.n[0] == 1:
            string = str(self.m)
        else:
            string = str(self.m)+'/'+str(self.n)
        return string
        

class Polinomial (list):
    def __init__ (self, m = 0, a0=Rational(), *args):
        self.m = m
        args = list(args)
        args.insert(0, a0)
        super().__init__(args)
        
    
    def copy(self):
        return Polinomial(self.m, *super().copy())
    
    
    def __str__(self):
        p = self.copy()
        p.reverse()
        string = ''
        for i in range(p.m):
            # Если числитель не ноль
            if p[i].m.n != 0 or p[i].m[0] != 0:
                string += str(p[i])+"x^"+str(p.m-i)
                
        if p[p.m].m.n != 0 or p[p.m].m[0] != 0:
            string += str(p[p.m])
        
        if string == '':
            string = '0'
        elif string[0] == '+':
            string = string[1::]
        return string
