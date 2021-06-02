def PrintBoxByWidth(n):
    # function created to prevent repeticion of print x statment.
    def print_x_line():
        print("x", end='')
    # loop determining number of lines.
    for line in range(0,5):
        print_x_line()
        # logic dictating to use given print statment on their determined line.
        if line == 1 or line == 3:
            for x in range(2,n):
                print(" ", end='')
            print_x_line()
        if line == 2:
            for x in range(2,n):
                print("o", end='')
            print_x_line()
        if line == 0 or line == 4:
            for x in range(1,n):
                print_x_line()
        print("")

PrintBoxByWidth(60)

# def main(n):
#     line =  "x"*(n+2)
#     print (line)
#     s = "x" + "o"*(n) + "x"
#     v = "x" + " "*(n) + "x"
#     print(v)
#     print(s)
#     print(v)
#     print(line)
    

# def main(n):
#     line =  "x"*(n+2)
#     print (line)
#     s  = "x" + "o"*(n) + "x"
#     for i in range(0,3):
#         print (s)
#     print (line)