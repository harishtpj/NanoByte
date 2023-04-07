# Nanobyte helper methods

def revstr(s):
    reversed_s = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s

def assemble(program):
    prgm_arr = []
    for line in program.split("\n"):
        if line[0] == "$":
            if line[1:3] == "0b":
                prgm_arr.append(int(line[1:], 2))
            elif line[1:3] == "0o":
                prgm_arr.append(int(line[1:], 8))
            elif line[1:3] == "0x":
                prgm_arr.append(int(line[1:], 16))
            else:
                prgm_arr.append(int(line[1:]))
                
        elif line[0] == ".":
            for chr in line[1:]:
                prgm_arr.append(ord(chr))
                
        else:
            for i in line.split():
                prgm_arr.append(int(i))
    return prgm_arr
    