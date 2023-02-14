class EmptyError(Exception): pass
#1
from prednaska import Stack
s = Stack()
#s.push(8); s.push(9); s.push(10); s.pop(); s.push(7); s.push(6); s.pop()
#s.pop(); s.push(2); s.push(3); s.pop(); s.pop(); s.pop(); s.pop(); s.pop()
#2

for i in 7,2,0,4:
    s.push(i)
    s.push(i + 1)
#while not s.is_empty():
    #print(s.pop(), end=' ')

#3
d=Stack([123])

#4
def pocet_cisel(sta):
    pocet = 0

    while not sta.is_empty():
        typ = type(sta.pop())
        if typ == int or typ == float:
            pocet += 1
    return pocet

s = Stack("py")

#5
def pocet_prvkov(zasobnik):
    pocet = 0
    kopia = Stack()                   # pomocný zásobník
    while not zasobnik.is_empty():
        kopia.push(zasobnik.pop())
        pocet += 1
    while not kopia.is_empty():       # vráti pôvodný obsah zásobníka
        zasobnik.push(kopia.pop())
    return pocet
def druhy(stack):
    pocet_gut = pocet_prvkov(stack)
    kopia = Stack()
    pocet = 0
    vysledok = None
    while not stack.is_empty():
        pocet += 1
        if pocet_gut - 1 == pocet:
            vysledok = stack.pop()
        else:
            kopia.push(stack.pop())

    while not kopia.is_empty():  # vráti pôvodný obsah zásobníka
        stack.push(kopia.pop())
    if vysledok is None:
        raise EmptyError
    else:
        return vysledok
#6
def prevrat(stack):
    