# Display methods for memory
from microbit import display
import helpers

# Function to display a specific memory location
def mem_location(mloc):
    mloc = ("{a:10b}".format(a=mloc))
    for p in range(len(mloc)):
        if mloc[p] == '1':
            if p > 4:
                display.set_pixel(p - 5, 4, 9)
            else:
                display.set_pixel(p, 3, 9)

# Function to display memory content
def mem_content(mcontent):
    mcontent = ("{a:08b}".format(a=mcontent))
    for p in range(len(mcontent)):
        if mcontent[p] == '1':
            if p > 4:
                display.set_pixel(p - 4, 1, 9)
            else:
                display.set_pixel(p, 0, 9)

# Function to clear the above
def clear_mem_disp(type):
    if type == "mloc":
        for y in range(3,5):
            for x in range(5):
                display.set_pixel(x, y, 0)
    elif type == "mcontent":
        for y in range(2):
            for x in range(5):
                display.set_pixel(x, y, 0)

# Function to Clear Full screen
def clear_scr():
    clear_mem_disp("mloc")
    clear_mem_disp("mcontent")
    display.set_pixel(2, 2, 0)
    display.set_pixel(0, 2, 0)
    display.set_pixel(1, 2, 0)
