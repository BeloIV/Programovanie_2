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
            if int(value)<0 or len(str(value)):
                x = int(value)%(256**self.num_bytes)
            else:
                x = int(value)
            self._mem[address] = int(x)







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
                x = int(self.reg.get(int(param[0])))
                y = int(self.reg.get(int(param[1])))
                self.reg.set(int(param[1]),x)
            elif instr == "load":
                x = int(self.reg.get(int(param[1])))
                self.reg.set(int(param[0]), x)
        return pc + 1

prog1 = '''
    read 0
    read 1
    store 0 2
    const 3 1
    jz 1 9
    mul 0 2
    sub 1 3
    jl 3 1 6
    print 0
    print 3
'''

prog2 = '''
'''

if __name__ == '__main__':
    ram = RAM(prog1)
    print(ram.start('42 0'))


