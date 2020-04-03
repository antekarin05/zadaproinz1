class Razlomak(object):
    '''Klasa razlomak'''
    def __init__(self, brojnik, nazivnik = 1):
        if nazivnik == 0:
            raise Exception('Nazivnik ne moze biti 0')
        self._brojnik = brojnik
        self._nazivnik = nazivnik

    def __str__(self):
        return '%d|%d' % (self._brojnik, self._nazivnik) 

    @staticmethod
    def inverz(razlomak):
        return '%d|%d' % (razlomak._nazivnik, razlomak._brojnik)

    @staticmethod
    def stvori(br):
        dec = 0
        naz = 10
        while (br % 1 != 0):
            br *= 10
            dec += 1
            naz = pow(naz, dec)   
        return Razlomak(br, naz)


print('*** test1 ***')
r1 = Razlomak(314,100)
print(r1)
r2 = Razlomak.inverz(r1)
print(r1,r2,r1)


print('*** test2 ***')
r1 = Razlomak.stvori(3.14)
print(r1)
r2 = Razlomak.stvori(0.006021)
print(r2)
r3 = Razlomak.stvori(-75.204)
print(r3)