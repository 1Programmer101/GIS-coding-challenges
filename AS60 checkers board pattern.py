n = int(input("row length:"))
m = int(input("column length"))

asterisk = False
start_ast = False

for x in range(n):
    for y in range(m):
        if asterisk == True:
            print("*", end="")
            asterisk = False
        else:
            print(".", end="")
            asterisk = True
    if start_ast == False:
        start_ast = True
        asterisk = True
    else:
        start_ast = False
        asterisk = False
    print("")
