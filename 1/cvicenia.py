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

s = Stack((5, '7', 3.14, [8]))
print(pocet_cisel(s))
#5

