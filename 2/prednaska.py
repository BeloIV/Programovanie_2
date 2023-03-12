class Vrchol:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

v1 = Vrchol(11)
v2 = Vrchol(22)
v3 = Vrchol(33)
v1.next = v2
v2.next = v3
del v2,v3
print(v1.data)
print(v1.next.data)
print(v1.next.next.data)

