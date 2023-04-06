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
        ndisplay.clear_scr()

        if vm.stepCount < 3:
            val = [vm.a, vm.b, vm.c][vm.stepCount]
            ndisplay.mem_location(vm.ip + vm.stepCount)

            if val == 0:
                display.set_pixel(0, 2, 9)
            elif val == -1:
                display.set_pixel(1, 2, 9)
            else:
                ndisplay.mem_content(val)

        if vm.stepCount >= 2:
            vm.stepCount = 0
        else:
            vm.stepCount += 1

        sleep(500)


    if button_a.is_pressed():
        vm.exec()

    
