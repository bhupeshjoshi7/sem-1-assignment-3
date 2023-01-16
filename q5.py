string = "ABCDEFGHIJK"
j = 0
while len(string)-j*2 >= 1:
    print(" "*j, string[0 : len(string) - j*2])
    j += 1