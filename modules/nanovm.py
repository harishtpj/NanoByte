# URSIC based NanoByte VM
from microbit import display
import helpers

class NanoByteVM:
    def __init__(self):
        self.ip = 0
        self.memory = [0] * 1024
        self.isRunning = True
        self.a = -1
        self.b = -1
        self.c = -1
        self.stepCount = 0
        
    def load(self, program):
        program = helpers.assemble(program)
        self.memory[:len(program)] = program

    def step(self):
        if self.ip == -1:
            self.isRunning = False
            display.show("Program completed")
        else:
            self.a = self.memory[self.ip]
            self.b = self.memory[self.ip + 1]
            self.c = self.memory[self.ip + 2]

    def exec(self):
        self.isRunning = True
        if self.a == -1:
            raise NotImplemented("Not yet Input Feature Created")
        elif self.b == -1:
            display.scroll(chr(self.memory[self.a]))
        else:
            self.memory[self.b] -= self.memory[self.a]
            if self.memory[self.b] <= 0:
                self.ip = self.c - 3
        self.ip += 3
        display.scroll(self.ip)
                
