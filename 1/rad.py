class EmptyError(Exception): pass

class Queue:

    def __init__(self):
        '''inicializuje zoznam'''
        self._prvky = []

    def enqueue(self, data):
        '''na koniec radu vloží novú hodnotu'''
        self._prvky.append(data)

    def dequeue(self):
        '''zo začiatku radu vyberie prvú hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny rad')
        return self._prvky.pop(0)

    def front(self):
        '''zo začiatku radu vráti prvú hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny rad')
        return self._prvky[0]

    def is_empty(self):
        '''zistí, či je rad prázdny'''
        return self._prvky == []

