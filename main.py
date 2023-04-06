# NanoByte - A Simple 8bit processor
from microbit import *
import ndisplay, nanovm

program = [15, 17, -1, 17, -1, -1, 16, 1, -1, 16, 3, -1, 15, 15,
            0, 0, -1, 72, 101, 108, 108, 111, 44, 32, 119, 111,
            114, 108, 100, 33, 10, 0]

vm = nanovm.NanoByteVM()
display.scroll("NanoByte is Ready!")

vm.load(program)
display.scroll("Program Loaded.")

while True:
    if vm.isRunning == True:
        display.set_pixel(4, 2, 9)
    else:
        display.set_pixel(4, 2, 0)
        break
        
    if button_b.is_pressed():
        vm.step()
        ndisplay.clear_mem_disp("mloc")
        ndisplay.clear_mem_disp("mcontent")

        for loc, val in enumerate([vm.a, vm.b, vm.c]):
            if (vm.ip + loc) == 0:
                display.set_pixel(2, 2, 9)
            else:
                ndisplay.mem_location(vm.ip + loc)

            if val == 0:
                display.set_pixel(0, 2, 9)
            elif val == -1:
                display.set_pixel(1, 2, 9)
            else:
                ndisplay.mem_content(val)

            sleep(15000)
            ndisplay.clear_scr()
        
