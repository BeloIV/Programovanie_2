"""x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(iter(x))
for i in range(9):
    x.append(i)

print(x)

"""
pole = [2, 3, 5, 7, 11, 13, 17]
"""for i in pole:
    print(i, i*i)"""
"""iterator = iter(pole)
while True:
    try:
        i = next(iterator)
        print(i, i*i)
    except StopIteration:
        break"""
def prvo():
    yield from [2, 3, 5, 7, 11]


def test(n):
    yield from range(n + 1)
    yield from range(n - 1, -1, -1)

def urob(n):
    if n < 1:
        yield 0
    else:
        yield n
        yield from urob(n-1)
        yield n


def fib(n):
    a, b = -1, 1
    while n > 0:
        a, b = b, a+b
        yield b
        n -= 1

"""
for i in fib(10000):
        print(i, end=' ')
        if i > 10000:
            break"""

class Moj:
    def __init__(self):
        self.p = []

    def append(self, x):
        self.p.append(x)

    def __getitem__(self, i):
        return self.p[i]


"""a = Moj()
for i in 'Python':
    a.append(i)
print(a)
for i in a:
        print(i, end=' ')
it = iter(a)"""
"""while 1:
        try:

            next(it)
        except StopIteration:
            break"""

zoznam = [i for i in range(20) if i%7 in [2,3,5]]
print(zoznam)