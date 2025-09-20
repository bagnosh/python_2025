import math

class Fraction:
    def __init__(self,n,d):
        self._n = n
        self._d = d
        self.neat()
    
    def neat(self):
        gcd = math.gcd(int(self._n), int(self._d))
        self._n /= gcd
        self._d /= gcd

    @property
    def d(self):
        return self._d
    
    @property
    def n(self):
        return self._n
    
    @d.setter
    def d(self, value):
        if value == 0:
            raise ValueError("Denominator cannot be 0")
    
    def __mul__(self, other):
        new_n = self._n * other._n
        new_d = self._d * other._d
        return Fraction(new_n,new_d)
    
    def __truediv__(self, other):
        new_n = self._n * other._d
        new_d = self._d * other._n
        return Fraction(new_n,new_d)
    
    def __add__(self, other):
        new_n = (self._n * other._d) + (other._n * self._d)
        new_d = self._d * other._d
        return Fraction(new_n,new_d)
    
    def __sub__(self, other):
        new_n = (self._n * other._d) - (other._n * self._d)
        new_d = self._d * other._d
        return Fraction(new_n,new_d)
    
    def __repr__(self):
        return(f"{int(self._n)}/{int(self._d)}")

'''
#example:
fra1 = Fraction(4,8)
fra2 = Fraction(3,5)

print(f"1: {int(fra1.n)}/{int(fra1.d)}")
print(f"2: {int(fra2.n)}/{int(fra2.d)}")

fra3 = fra1 + fra2
fra4 = fra1 - fra2
fra5 = fra1 * fra2
fra6 = fra1 / fra2

print(f"3: {int(fra3.n)}/{int(fra3.d)}")
print(f"4: {int(fra4.n)}/{int(fra4.d)}")
print(f"5: {int(fra5.n)}/{int(fra5.d)}")
print(f"6: {int(fra6.n)}/{int(fra6.d)}")
'''