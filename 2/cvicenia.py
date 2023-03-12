#1
class Vrchol:
    def __init__(self, data, next=None):
        self.data, self.next = data, next
def vypis(zoznam):
    while zoznam is not None:
        print(repr(zoznam.data), end=' -> ')
        zoznam = zoznam.next
    print(None)
def vyrob(postupnost):
    zoz = None
    for hodnota in reversed(postupnost):
        zoz = Vrchol(hodnota, zoz)
    return zoz
#2
v3 = Vrchol('3.14',Vrchol('6.28',Vrchol('9.42',Vrchol(None,Vrchol('15.7',)))))
v2 = vyrob(['3.14','6.28','9.42',None,'15.7'])
#3
zoz = vyrob(range(4,26,7))

def zmen(zoznam,ktory, na_hodnotu):
    teraz=1
    while zoznam is not None:
        if teraz == ktory:
            zoznam.data = na_hodnotu
        teraz +=1
        zoznam = zoznam.next
#4
v = vyrob('strc prst skrz krk'.split())
def pridaj_pred(zoznam, kde, hodnota):
    if zoznam is None:
        return None                       # nie je čo robiť
    pred, pom = None, zoznam
    teraz = 1
    while pom is not None and teraz != kde:
        pred, pom = pom, pom.next
        teraz += 1
    if kde == 1 or pred is None:
        zoznam = Vrchol(hodnota, zoznam)  # pred prvý
    elif pom is not None :
        pred.next = Vrchol(hodnota, pred.next)


    return zoznam
v = pridaj_pred(v,4,"SDFGH")
#5
v5 = vyrob([5,0,2.12,"2",18,4.0,4])
def zmen(zoznam,na=0):
    while zoznam is not None:
        try:
            if zoznam.data%2 == 0:
                zoznam.data = na
            zoznam = zoznam.next
        except:
            zoznam = zoznam.next

#6
def pocty(zoznam,hodnota=0):
    vacia = 0
    mensia = 0
    while zoznam is not None:
        try:
            if zoznam.data> hodnota:
                vacia +=1
            elif zoznam.data<hodnota:
                mensia +=1
            zoznam = zoznam.next
        except:
            zoznam = zoznam.next
    return (vacia,mensia)
zozn = vyrob([0,2,5,45,2,"ko","Konec"])
#7
def zdvoj(zoznam):
    while zoznam is not None:
        try:
            zoznam.data = zoznam.data *2
            zoznam = zoznam.next
        except:
            zoznam = zoznam.next
    return zoznam

#8
def to_str(zoznam):
    zoz = []
    while zoznam is not None:
        zoz.append(zoznam.data)
        zoznam = zoznam.next


    zoz = " -> ".join(zoz)
    zoz += " -> "+"None"



#9
"""zoz = vyrob((1, 3, 5, 7, 9, 11, 13))
v = zoz.next.next
v1 = v.next.next

v.next.next = v1.next
v1.next = v.next
v.next = v1
vypis(zoz)"""
#10
def vyhod_prvy(zoznam):
    zoz = []
    while zoznam is not None:
        zoz.append(zoznam.data)
        zoznam = zoznam.next
    zoz = zoz[1:]
    zoznam = vyrob(zoz)
    return zoznam
#11
def vyhod_druhy(zoznam):
    zoz = []
    while zoznam is not None:
        zoz.append(zoznam.data)
        zoznam = zoznam.next

    zoz.remove(zoz[1])

    zozna = vyrob(zoz)
    return zozna
#13
def vyhod_posledny(zoznam):
    zoz = []
    while zoznam is not None:
        zoz.append(zoznam.data)
        zoznam = zoznam.next
    zoz.remove(zoz[-1])
    zoznam = vyrob(zoz)
    return zoznam

#14
def vyhod_kazdy_druhy(zoznam):
    zoz = []
    while zoznam is not None:
        zoz.append(zoznam.data)
        zoznam = zoznam.next
    for cis,i in enumerate(zoz):
        if cis%2==0:
            zoz.remove(i)
    zoznam = vyrob(zoz)
    return zoznam
#17
def spoj(zoz1,zoz2):
    while zoz2 is not None:
        print(zoz2.data)
        zoz1 = Vrchol(zoz2.data,zoz1)
        zoz2 = zoz2.next

    return zoz1
vypis(zozn)
zoz1 = vyhod_prvy(zozn)
vypis(zoz1)
g = spoj(zozn,zoz1)
vypis(g)