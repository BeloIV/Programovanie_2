# 2. zadanie: ram
# autor: Stefan Belusko
# datum: 3.3.2023

class RAMError(Exception): pass

class Registers:
    def __init__(self, num_bytes, maximum):
        self._mem = []
        self.maxim = maximum
        self.num_bytes = num_bytes


    def get(self, address):
        try:
            return self._mem[address]
        except:
            return 0

    def set(self, address, value):

        if address<self.maxim:

            if len(self._mem)<=address:

                for i in range(address-len(self._mem)+1):
                    self._mem.append(0)

            if value<0 or len(str(value)):
                x = value%(256**self.num_bytes)
            else:
                x = value

            self._mem[address] = int(x)


    def __len__(self):
        return len(self._mem)

    def __repr__(self):


        vypis = "reg: "
        for i in self._mem:
            vypis +=str(i)+" "
        return vypis

class RAM:
    def __init__(self, program):
        program = program.split("\n")
        for cis,i in enumerate(program):
            if "#" in i:
                i = i[:i.index("#")]
            i = i.strip()
            program[cis]=i.split()

        self.program = []
        for i in program:
            if i != []:
                self.program.append(i)


    def start(self, input='', num_bytes=2, maximum=1000):
        self.reg = Registers(num_bytes, maximum)

        self.vypis = []
        self.paska = input.split()
        self.index_pasky = 0
        pc = 0
        self.stop = 0
        self.index_programu = 0
        self.yes = True
        while self.yes is True:
            if self.index_programu < len(self.program):
                if self.program[self.index_programu] != []:
                    i = self.program[self.index_programu]
                    pc = self.instruction(pc,i[0],i[1:])
                    self.index_programu += 1
            else:
                self.yes = False

        return self.vypis


    def __repr__(self):
        return repr(self.reg)

    def instruction(self, pc, instr, *param):

        if self.yes is True:
            par= []
            for i in param:
                for x in i:
                    par.append(x)
            param = par
            if instr== "halt":
                self.yes = False
            elif instr == "nop":
                pass
            elif instr == "read":
                try:
                    self.reg.set(int(param[0]),int(self.paska[self.index_pasky]))
                    self.index_pasky += 1
                except:raise RAMError

            elif instr == "print":
                x = self.reg.get(int(param[0]))
                self.vypis.append(x)
            elif instr == "const":
                self.reg.set(int(param[0]), int(param[1]))
            elif instr == "add":
                x = int(self.reg.get(int(param[0])))
                y = int(self.reg.get(int(param[1])))
                self.reg.set(int(param[0]), x+y)
            elif instr == "sub":
                x = int(self.reg.get(int(param[0])))
                y = int(self.reg.get(int(param[1])))

                self.reg.set(int(param[0]), x - y)
            elif instr == "mul":
                x = int(self.reg.get(int(param[0])))
                y = int(self.reg.get(int(param[1])))

                self.reg.set(int(param[0]), x * y)
            elif instr == "div":

                try:
                    x = int(self.reg.get(int(param[0])))
                    y = int(self.reg.get(int(param[1])))

                    self.reg.set(int(param[0]), x // y)
                except:raise RAMError
            elif instr =="jump":
                self.index_programu = int(param[0])-1
            elif instr == "jz":
                x = int(self.reg.get(int(param[0])))
                if x == 0:
                    self.index_programu = int(param[1])-1
            elif instr == "jnz":
                x = int(self.reg.get(int(param[0])))
                if x != 0:
                    self.index_programu = int(param[1])-1
            elif instr == "jl":
                x = int(self.reg.get(int(param[0])))
                y = int(self.reg.get(int(param[1])))

                if x <y:
                    self.index_programu = int(param[2])-1
            elif instr =="store":
                while int(self.reg.get(int(param[0]))) >= len(self.reg):
                    self.reg.set(len(self.reg), 0)
                x = self.reg.get(int(param[0]))
                self.reg.set(x,self.reg.get(int(param[1])))

            elif instr == "load":
                x = int(self.reg.get(int(param[1])))
                self.reg.set(int(param[0]), x)
            elif instr == "power":
                x = int(self.reg.get(int(param[0])))
                y = int(self.reg.get(int(param[1])))
                self.reg.set(int(param[0]), x ** y)
            elif instr == "count":
                x = self.reg.get(int(param[0]))
                y= 0
                for i in self.paska:
                    if int(i) >x:
                        y +=1
                self.reg.set(int(param[1]),y)

        return pc + 1

prog1 = '''
    read 0
    read 1
    power 0 1
    print 0
'''

prog2 = '''
    const 1 0 #pocet
    const 2 0 #sucet
    const 3 0 #priemer 
    const 4 0 #pocet viac ako
    const 5 1 # just a 1 
    read 0 # cita zo vstupu
    add 1 5 # pocet +=1
    add 2 0 # sucet += read
    add 3 0 # sucet na priemer +=read 
    jnz 0 4 #
    sub 1 5 # skac hore ak nieje read 0
    div 3 1 # sucet na priemer//pocet
    count 3 4 # pocet viac ako priemer 
    print 1 
    print 2
    print 3
    print 4
'''
if __name__ == '__main__':
    ram = RAM(prog2)
    print(ram.start('1 2 4 0', 1))
    print(ram.reg)# vstupná páska '8', počet bajtov pre registre je 1
