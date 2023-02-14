class EmptyError(Exception): pass

class Stack:

    def __init__(self,postupnost=None):
        '''inicializuje zoznam'''
        self._prvky = []

        if postupnost is not None:
            for i in postupnost:
                self.push(i)

    def __repr__(self):
        return f' Stack({tuple(self._prvky)})'


    def push(self, data):
        '''na vrch zásobníka vloží novú hodnotu'''
        self._prvky.append(data)

    def pop(self):
        '''z vrchu zásobníka vyberie hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny zasobnik')
        return self._prvky.pop()

    def top(self):
        '''z vrchu zásobníka vráti hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny zasobnik')
        return self._prvky[-1]

    def is_empty(self):
        '''zistí, či je zásobník prázdny'''
        return self._prvky == []

def pocitaj(vyraz):
    s = Stack()
    for prvok in vyraz.split():
        if prvok == '+':
            s.push(s.pop() + s.pop())
        elif prvok == '-':
            s.push(-s.pop() + s.pop())
        elif prvok == '*':
            s.push(s.pop() * s.pop())
        elif prvok == '/':
            op2 = s.pop()             # môžeme zapísať aj: op2, op1 = s.pop(), s.pop()
            op1 = s.pop()
            s.push(op1 // op2)
        else:
            s.push(int(prvok))
    return s.pop()
