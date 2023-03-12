# 1. zadanie: vyraz
# autor: Janko Hrasko
# datum:

class Expression:
    def __init__(self):
        self.tab = {}
        self.vyratane_premenne ={}
        self.stop_rekurzie = 0
        self.fghldf = 0

    def __repr__(self):
        vypis = ""
        for i in self.tab.keys():
            vypis += f'{i}: '+f"'{self.tab[i]}'"+ '\n'
        vypis = vypis.strip()
        return vypis

    def zisti_co_je_to_zas(self, expr):
        """Zisti aky tvar bol zadany"""
        expr = expr.replace(" ", "")
        if expr[0] in "* + / % //-":
            return "prefix"
        elif expr[-1] in "*+-/%//":
            return "postfix"
        elif expr[0].isalnum() or  expr[0] in "()" :
            return "infix"
        if expr[0] in "-" and expr[1] in "*+/%//":
            return "prefix"
        elif expr[0] in "-" and expr[1] in "0123456789":
            return "infix"

    def daj_medzeri(self,text):
        """Da po 1 medzere tam kde maju byt"""
        vypis = []
        daj = ""
        pridane =0
        bolo = 0

        for i in text:
            if i.isalnum():
                daj += i
                pridane = 0
            elif i in "*+-/%//() ":
                bolo = 1
                if daj != " " and daj != "":
                    vypis.append(daj)
                daj = ""
                if i !=" " and i !="":
                    vypis.append(i)
                pridane = 1
        if bolo == 0:
            return [text]
        if pridane == 0:
            vypis.append(daj)
        return vypis
    def to_prefix(self, expr):
        co_je_to = self.zisti_co_je_to_zas(expr)

        if co_je_to == "prefix":
            vypis = []
            daj=None
            for i in expr:
                if i in "*+-/%//":
                    vypis.append(i)
                elif i ==" " and daj !=None:
                    vypis.append(daj)
                    daj = None
                else:
                    if i != " ":
                        if daj == None:
                            daj = ""
                        daj += i
            if daj != None:
                vypis.append(daj)
                daj = None
            try:
                vypis = " ".join(vypis)
                vypis = vypis.split()
                vyp = ""

                for i in vypis:
                    vyp += i + " "
                vyp = vyp.strip()
                return vyp
            except:
                return None
        elif co_je_to == "infix":

            expr = self.daj_medzeri(expr)

            vypis =[]
            zasobnik =[]
            for i in reversed(expr):
                if i.isalnum():
                    vypis.append(i)
                elif i == ")":
                    zasobnik.append(i)
                elif i == "(":
                    x= 0
                    while x == 0:
                        if zasobnik[-1] == ")":
                            x =1
                            zasobnik.pop(-1)
                        else:
                            vypis.append(zasobnik.pop(-1))
                elif i in "*+-/%//":
                    if zasobnik==[] :
                        zasobnik.append(i)
                    elif self.zisti_prioritu(zasobnik[-1])>self.zisti_prioritu(i):

                        try:
                            while self.zisti_prioritu(zasobnik[-1])>self.zisti_prioritu(i) :
                                vaa = zasobnik.pop(-1)
                                vypis.append(vaa)
                            zasobnik.append(i)
                        except:
                            zasobnik.append(i)
                    elif self.zisti_prioritu(zasobnik[-1])<=self.zisti_prioritu(i):
                        zasobnik.append(i)
            try:
                while True:
                    vypis.append(zasobnik.pop(-1))
            except:
                pass

            vysledok = []
            for i in reversed(vypis):
                vysledok.append(i)
            vypis = vysledok
            try:
                vypis = " ".join(vypis)
                vypis = vypis.split()
                vyp = ""

                for i in vypis:
                    vyp += i + " "
                vyp = vyp.strip()
                return vyp
            except:
                return None

        elif co_je_to == "postfix":
            zasobnik = []
            for i in expr:
                if i.isalnum():
                    zasobnik.append(i)
                elif i in "*+-/%//":
                    vloz= ""
                    for x in range(2):
                        vloz = str(zasobnik.pop(-1))+" " + vloz
                    vloz = str(i) +" "+ vloz

                    zasobnik.append(vloz)
            vypis = zasobnik
            try:
                vypis = " ".join(vypis)
                vypis = vypis.split()
                vyp = ""

                for i in vypis:
                    vyp += i + " "
                vyp = vyp.strip()
                return vyp
            except:
                return None
    def zisti_prioritu(self,znak):
        jeden = "+-"
        dva = "*/%"
        nula = "()"
        if znak in jeden:
            return 1
        elif znak in dva:
            return 2
        elif znak in nula:
            return 0

    def assign(self, var, expr):
        expr = self.to_prefix(expr)
        self.tab[var] = expr
        try:
            x = self.evaluate(expr)
            if x is not None:
                self.vyratane_premenne[var] = x

        except:
             pass
    def evaluate(self,expr):
        expr = self.to_prefix(expr)
        pomoc = expr.split()
        for i in pomoc:

            if i[0].isalpha():

                try:
                    x = self.evalu(self.tab[i])
                    if x is not None:
                        self.vyratane_premenne[i] = x
                except:
                    pass
            try:
                ff = self.tab[i]

                try:
                    x = self.vyratane_premenne[ff]
                except:

                    if self.stop_rekurzie != self.tab[i] and self.fghldf<=100:
                        for ggf in ff:
                            if ggf[0].isalpha():
                                try:
                                    y = self.evalu(self.tab[ggf])
                                    if y is not None:
                                        self.vyratane_premenne[ggf] = y
                                        self.fghldf += 1

                                        self.evaluate(expr)

                                except:pass
                    self.stop_rekurzie = self.tab[i]

            except:pass

        try:
            return int(self.evalu(expr))
        except:
            pass
    def evalu(self, expr):
        try:
            try:
                toto_je_ono = self.vyratane_premenne[expr]
                if toto_je_ono is not None:
                    return toto_je_ono
            except:
                pass
            zasobnik = []
            expr = self.to_prefix(expr)
            expr = expr.split()
            for i in reversed(expr):
                if i[0].isalpha():

                   try:
                       zasobnik.append(self.vyratane_premenne[i])
                   except:
                       return None
                elif i.isnumeric():
                    zasobnik.append(i)
                elif i in "-*+/%//":
                    for cis,x in enumerate(range(2)):
                        if cis == 0:
                            cislo1= int(zasobnik.pop(-1))
                        else:
                            cislo2 = int(zasobnik.pop(-1))
                    if i == "*":
                        zasobnik.append(cislo1*cislo2)
                    elif i == "+":
                        zasobnik.append(cislo1+cislo2)
                    elif i == "-":
                        zasobnik.append(cislo1-cislo2)
                    elif i == "/":
                        zasobnik.append(cislo1//cislo2)
                    elif i == "%":
                        zasobnik.append(cislo1%cislo2)
            return zasobnik[0]
        except:
            pass


if __name__ == '__main__':
    e = Expression()
    e.assign('x', 'y*(y-1)')
    e.assign('y', '3+4*5')
    print(e)
    print('x =', e.evaluate('x'))
    print('y =', e.evaluate('y'))
    e.assign('y', '9*9%6')
    print(e)
    for name in e.tab:
        print(name, '=', e.evaluate(name))