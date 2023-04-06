# URSIC based NanoByte VM
from microbit import display

class NanoByteVM:
    def __init__(self):
        self.ip = 0
        self.memory = [0] * 1023
        self.isRunning = True
        self.a = -1
        self.b = -1
        self.c = -1
        
    def load(self, program):
        self.memory[:len(program)] = program
        self.memory[len(program)+1] = -9

    def step(self):
        self.a = self.memory[self.ip]
        self.b = self.memory[self.ip + 1]
        self.c = self.memory[self.ip + 2]

    def exec(self):
        self.isRunning = True
        if -9 in [self.a, self.b, self.c]:
            self.isRunning = False
            display.show("Program completed")
        elif self.a == -1:
            raise NotImplemented("Not yet Input Feature Created")
        elif self.b == -1:
            display.show(chr(self.memory[self.a]), delay=1000)
        else:
            self.memory[self.b] -= self.memory[self.a]
            if self.memory[self.b] <= 0:
                self.ip = self.c
            else:
                self.ip += 3
                
