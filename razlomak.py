from fractions import Fraction

class Razlomak(object):
    def __init__(self, brojnik, nazivnik):
        self._brojnik=brojnik
        self._nazivnik=nazivnik
    
    @property
    def brojnik(self):
        return self._brojnik
    
    @brojnik.setter
    def brojnik(self, value):
        self._brojnik=value

    @property
    def nazivnik(self):
        return self._nazivnik
    
    @nazivnik.setter
    def nazivnik(self, value):
        self._nazivnik=value

    def skrati(self):
        b=self._brojnik
        n=self._nazivnik
        while b%n !=0:
            b, n = n, b % n
        t=n
        self._brojnik //=t
        self._nazivnik //=t



    def __str__(self):
        return str(self._brojnik)+"|"+str(self._nazivnik)

    def __repr__(self):
        return "Razlomak("+repr(self._brojnik)+","+repr(self._nazivnik)+")"
    


    def __eq__(self,other):
        return self.brojnik/self.nazivnik== other.brojnik/other.nazivnik

    def __lt__(self,other):
        return self.brojnik/self.nazivnik< other.brojnik/other.nazivnik

    def __le__(self,other):
        return self.brojnik/self.nazivnik<= other.brojnik/other.nazivnik

    def __add__(self,other):
        return Fraction(self.brojnik, self.nazivnik) + Fraction(other.brojnik, other.nazivnik)

    def __sub__(self,other):
        return Fraction(self.brojnik, self.nazivnik) - Fraction(other.brojnik, other.nazivnik)

    def __mul__(self,other):
        return Fraction(self.brojnik, self.nazivnik) * Fraction(other.brojnik, other.nazivnik)

    def __truediv__(self,other):
        return Fraction(self.brojnik, self.nazivnik) / Fraction(other.brojnik, other.nazivnik)

# Zadtak1.1

print('*** test 1 ***')
r1 = Razlomak(12,30)
print(r1.brojnik, r1.nazivnik)
r1.skrati()
print(r1.brojnik, r1.nazivnik)

# Zadatak 1.2
print('*** test 2 ***')
r1 = Razlomak(12,30)
r2 = Razlomak(2,5)
r3 = Razlomak(3,6)
print(r1,r2,repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(3,4)+Razlomak(5,2))
print(Razlomak(1,3)-Razlomak(2,6))
print(Razlomak(2,8)*Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))