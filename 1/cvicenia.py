class EmptyError(Exception): pass


# 1
from prednaska import Stack

s = Stack()
# s.push(8); s.push(9); s.push(10); s.pop(); s.push(7); s.push(6); s.pop()
# s.pop(); s.push(2); s.push(3); s.pop(); s.pop(); s.pop(); s.pop(); s.pop()
# 2

for i in 7, 2, 0, 4:
    s.push(i)
    s.push(i + 1)
# while not s.is_empty():
# print(s.pop(), end=' ')

# 3
d = Stack([123])


# 4
def pocet_cisel(sta):
    pocet = 0

    while not sta.is_empty():
        typ = type(sta.pop())
        if typ == int or typ == float:
            pocet += 1
    return pocet


s = Stack("py")


# 5
def pocet_prvkov(zasobnik):
    pocet = 0
    kopia = Stack()  # pomocný zásobník
    while not zasobnik.is_empty():
        kopia.push(zasobnik.pop())
        pocet += 1
    while not kopia.is_empty():  # vráti pôvodný obsah zásobníka
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
# 7
# a)  2 * (2 + 1) * (2 + 1 + 1) * (2 + 1 + 1 + 1)
# prefix
    # * 2 + 2 1 * + 2 1 1 * + 2 1 1 1
# b) x % 10 * 100 + x // 10 % 10 * 10 + x // 100
# c)5 * 'a' + 'b' * 4
# d) 5 * ('a' + 'b') * 4

#9
def test(n):
    if n > 0:
        test(n-2)
        print(n, end='')
        test(n-1)
        print(n, end='')
test(5)
#10
def test2(n):
    stack = []
    while True:
        while n > 0:
            stack.append(n)
            n -= 2
        if not stack:
            break
        n = stack.pop()
        print(n, end='')
        n -= 1
        while n > 0:
            stack.append(n)
            n -= 2
        if not stack:
            break
        n = stack.pop()
        print(n, end='')
#11
import turtle

def strom(n):
    stack = []
    t.fd(5 * n)
    stack.append((n, 1))
    while stack:
        n, state = stack.pop()
        if n > 3 and state == 1:
            t.lt(40)
            stack.append((n, 2))
            stack.append((n - 1, 1))
        elif n > 3 and state == 2:
            t.rt(75)
            stack.append((n, 3))
            stack.append((n - 1, 1))
        elif n > 3 and state == 3:
            t.lt(35)
        else:
            t.bk(5 * n)
            if stack:
                n, state = stack.pop()
                if state == 1:
                    t.rt(75)
                    stack.append((n, 3))
                    stack.append((n - 1, 1))
                elif state == 2:
                    t.lt(35)
                elif state == 3:
                    pass

#12
def ckrivka(n, s):
    stack = [(n, s)]
    while stack:
        n, s = stack.pop()
        if n == 0:
            t.fd(s)
        else:
            stack.append((n - 1, s))
            stack.append((0, 0))
            stack.append((n - 1, s))
            t.lt(90)
            if stack:
                n, s = stack.pop()
                if n == 0:
                    t.fd(s)
                else:
                    stack.append((n - 1, s))
                    stack.append((0, 0))
                    stack.append((n - 1, s))
                    t.rt(90)

t = turtle.Turtle()
ckrivka(6, 20)





