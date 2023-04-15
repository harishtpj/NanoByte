# NanoByte - A Simple 8bit processor
from microbit import *
import ndisplay, nanovm, programs

vm = nanovm.NanoByteVM()
display.scroll("nB is Ready!")

vm.load(programs.nBPrint.hi())
display.scroll("Program Loaded.")

while True:
    if vm.isRunning == True:
        display.set_pixel(4, 2, 9)
    else:
        display.set_pixel(4, 2, 0)
        ndisplay.clear_scr()
        break
        
    if button_b.is_pressed():
        vm.step()
        ndisplay.clear_scr()

        if vm.stepCount < 3:
            val = [vm.a, vm.b, vm.c][vm.stepCount]
            ndisplay.mem_location(vm.ip + vm.stepCount)

            if val == -1:
                display.set_pixel(4, 1, 9)
            else:
                ndisplay.mem_content(val)

        if vm.stepCount >= 2:
            vm.stepCount = 0
        else:
            vm.stepCount += 1

        sleep(500)


    if button_a.is_pressed():
        vm.exec()

    
