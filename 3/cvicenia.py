#1
import random


class EmptyError(Exception): pass
class SpajanyZoznam:
    class Vrchol:
        def __init__(self, data, next=None):
            self.data, self.next = data, next

    def __init__(self, postupnost=None):
        self.zac = None                   # začiatok zoznamu
        if postupnost is not None:
            for hodnota in reversed(postupnost):
                self.insert0(hodnota)

    def __repr__(self):
        vysl, zoz = [], self.zac
        while zoz is not None:
            vysl.append(repr(zoz.data))
            zoz = zoz.next
        vysl.append('None')
        return ' -> '.join(vysl)

    def __len__(self):
        vysl, zoz = 0, self.zac
        while zoz is not None:
            vysl += 1
            zoz = zoz.next
        return vysl

    def __contains__(self, hodnota):
        zoz = self.zac
        while zoz is not None:
            if zoz.data == hodnota:
                return True
            zoz = zoz.next
        return False

    def insert0(self, hodnota):
        self.zac = self.Vrchol(hodnota, self.zac)

    def pop0(self):
        if self.zac is None:
            raise EmptyError
        vysl = self.zac.data
        self.zac = self.zac.next
        if self.zac is None:
            self.kon = None
        return vysl  # hodnota vyhodeného prvku

    def pop(self):
        if self.zac is None:
            raise EmptyError
        if self.zac.next is None:  # jednoprvkový zoznam
            vysl = self.zac.data
            self.zac = self.kon = None
            return vysl
        self.kon = self.zac
        while self.kon.next.next is not None:
            self.kon = self.kon.next
        vysl = self.kon.next.data
        self.kon.next = None
        return vysl
    def append(self, hodnota):
        if self.zac is None:
            self.zac = self.Vrchol(hodnota)
        else:
            posledny = self.zac
            while posledny.next is not None:
                posledny = posledny.next
            posledny.next = self.Vrchol(hodnota)

    def by_pattern(self,vzor=(0,)):
        index = 0
        zoz = self.zac
        while zoz is not None:
            zoz.data = vzor[index]
            if index == len(vzor)-1:
                index = 0
            else:
                index += 1
            zoz = zoz.next

    def count(self,podret):
        zoz = self.zac
        pocet=0
        while zoz is not None:
            if type(zoz.data) == str:
                for i in zoz.data:
                    if str(podret) in i:
                        pocet += 1

            zoz = zoz.next
        return pocet
    def copy(self):
        zoz = self.zac
        zoznam = []
        while zoz is not None:
            zoznam.append(zoz.data)
            zoz = zoz.next
        return SpajanyZoznam(zoznam)
    def reversed(self):
        zoz = self.zac
        zoznam = []
        while zoz is not None:
            zoznam.insert(0,zoz.data)
            zoz = zoz.next
        return SpajanyZoznam(zoznam)


    def filter(self,podmiena):
        zoz = self.zac
        zoznam = []
        while zoz is not None:
            if podmiena(zoz.data) is True:
                zoznam.append(zoz.data)
            zoz = zoz.next
        return SpajanyZoznam(zoznam)
    def map(self,funkcia):
        zoz = self.zac
        zoznam = []
        while zoz is not None:
            zoznam.append(funkcia(zoz.data))
            zoz = zoz.next
        return SpajanyZoznam(zoznam)
    def enumerate(self):
        zoz = self.zac
        zoznam = []
        cis = 0
        while zoz is not None:
            zoznam.append((cis,zoz.data))
            cis += 1

            zoz = zoz.next
        return SpajanyZoznam(zoznam)
    def opakuje_sa(self):

        zoz = self.zac

        zoznam = []

        while zoz is not None:
            zoz2 = zoz.next
            while zoz2 is not None:
                if zoz.data == zoz2.data:
                    if zoz.data not in zoznam:
                       zoznam.append(zoz.data)
                zoz2 = zoz2.next
            zoz = zoz.next
        try:
            return random.choice(zoznam)
        except:return None
    def __eq__(self, other):
        zoz = self.zac
        zoz2 = other.zac
        while zoz is not None:
            if zoz.data != zoz2.data:
                return False
            zoz2 = zoz2.next
            zoz = zoz.next
        try:


            if zoz2.data is not None:
                return False
        except:return True
        else:return True

    def _ity(self, index):  # pomocná metóda
        if index < 0:
            raise IndexError
        zoz = self.zac
        while zoz is not None and index > 0:
            zoz = zoz.next
            index -= 1
        if zoz is None:
            raise IndexError
        return zoz

    def __getitem__(self, index):  # vráti hodnotu i-teho prvku
        return self._ity(index).data

    def __setitem__(self, index, hodnota):  # zmení hodnotu i-teho prvku
        self._ity(index).data = hodnota

    def __delitem__(self,index):
        zoz = self.zac
        cis = 0
        while zoz is not None:
            print(cis,index)
            if cis == index:
                self.zac.next = self.zac.next.next
            cis +=1
            zoz = zoz.next


#2
"""z = SpajanyZoznam('PYTHON')
x = z.pop0()
y = z.pop()
z.append(x)
z.insert0(y)
print(z)"""
#3
"""
zoz = SpajanyZoznam('pocitac')
zoz.by_pattern('ab')
print(zoz)"""
#4
"""zoz = SpajanyZoznam('anicka dusicka kde si bola'.split())
for r in 'a', 'ic', 'kde si':
    print(repr(r), zoz.count(r))
print(SpajanyZoznam(('123', 232, '321', 433)).count('3'))
"""
#5
"""z = SpajanyZoznam('Python')
print(z)
z1 = z.copy()
print(z1)
z2 = z.reversed()
print(z2)
z3 = z.filter(lambda x: x in 'aeiouy')
print(z3)
z4 = z.map(lambda x: x.upper()+'!')
print(z4)
z5 = z.enumerate()
print(z5)"""
#6
class Paska:
    def __init__(self, obsah=''):
        self.paska = list(obsah or '_')
        self.poz = 0

    def symbol(self):
        return self.paska[self.poz]

    def zmen_symbol(self, znak):
        self.paska[self.poz] = znak

    def __str__(self):
        return ''.join(self.paska) + '\n' + ' '*self.poz + '^'

    def vpravo(self):
        self.poz += 1
        if self.poz == len(self.paska):
            self.paska.append('_')

    def vlavo(self):
        if self.poz > 0:
            self.poz -= 1
        else:
            self.paska.insert(0, '_')

    def text(self):
        return ''.join(self.paska).strip('_')

    symbol = property(symbol, zmen_symbol)
    text = property(text)

class Turing:
    def __init__(self, program, obsah='', start=None, koniec={'end', 'stop'}):
        self.program = {}
        self.stav = start
        for riadok in program.split('\n'):
            riadok = riadok.split()
            if len(riadok) == 5:
                stav1, znak1, znak2, smer, stav2 = riadok
                self.program[stav1, znak1] = znak2, smer, stav2
                if self.stav is None:
                    self.stav = stav1
        self.paska = Paska(obsah)
        self.koniec = koniec

    def __str__(self):
        return str(self.paska) + ' ' + self.stav

    def krok(self):
        stav1, znak1 = self.stav, self.paska.symbol
        try:
            znak2, smer, stav2 = self.program[stav1, znak1]
        except KeyError:
            return False
        self.paska.symbol = znak2
        self.stav = stav2
        if smer == '>':
            self.paska.vpravo()
        elif smer == '<':
            self.paska.vlavo()
        return True

    def rob(self, vypis=True):
        if vypis:
            print(self)
        while self.stav not in self.koniec:
            if not self.krok():
                return False
            if vypis:
                print(self)
        return True


"""(start, q)  ->  (q, >, jedna)
(jedna, q)  ->  (q, >, dva)
(dva, q)    ->  (q, >, start)
(jedna, _)  ->  (_, =, stop)"""
prog = '''
start q q > jedna
jedna q q > dva
dva q q > dva
dva q q > start
jedna _ _ = stop

'''
"""t = Turing(prog, 'qqqqqqqqqqqqqqqq')
t = Turing(prog, 'qqqqqqqqqqqqqqqqqqq')
t = Turing(prog, 'qqqqqqqqqqqqqqqqqqqqqq')
print(t.rob())"""
#7
"""
for retazec in 'abcb', 'ccccca', 'cba'*10, 'cbxcba', 'aabbccAABBCC':
    t = Turing('''
    ...
s1 a a > s1
s1 b b > s1
s1 c c > s1
s1 _ _ = stop
...
    ''', retazec)
    print(retazec, t.rob(False))"""
#8
"""prog = '''
q0 x x > q1
q1 x x > q0
q1 x x > q4
q4 x _ > end

'''

print(Turing(prog, 'xxx').rob())
print(Turing(prog, 'xx'*5).rob(False))
NEDA SA TO !!!!
"""
#9
"""to je rovnaka blbost jak ta 8 a chcem vidiet rieseie"""
#10
"""a = SpajanyZoznam((*range(100), *range(90, 200)))
print(a.opakuje_sa())
b = SpajanyZoznam('mama ma emu a ema Ma mamu'.split())
print(b.opakuje_sa())"""
#11
"""z1 = SpajanyZoznam(range(2, 7))
z2 = SpajanyZoznam((3, 4, 5, 6, 7))
z2.pop()
z2.insert0(2)
print(z1==z2)"""
#12
"""
import time

zoz1 = SpajanyZoznam(range(10000))
start = time.time()
z = zoz1.zac
while z is not None:
    z.data += 1
    z = z.next

koniec = time.time()
print('čas1 =', koniec - start)

zoz2 = SpajanyZoznam(range(10000))
start = time.time()
for i in range(len(zoz2)):
    zoz2[i] = zoz2[i] + 1
koniec = time.time()
print('čas2 =', koniec - start)

start = time.time()
list1 = list(SpajanyZoznam(range(10000)))
koniec = time.time()
print('list1 hotovo',koniec - start)
start = time.time()
zoz = SpajanyZoznam(range(10000))
list2 = []
z = zoz.zac
while z:
    list2.append(z.data)
    z = z.next
koniec = time.time()
print('list2 hotovo',koniec - start)
print(list1 == list2)
"""
#13
"""
z = SpajanyZoznam(range(3, 22, 4))
del z[2]
print(z)
"""
