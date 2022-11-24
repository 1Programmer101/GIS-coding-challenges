n = int(input("Upto what number do you want a times table for?\n"))
for rows in range(1, n+1):
    for columns in range(1, 11):
       print(rows, "X", columns, " = ", rows*columns, end=" || ", sep="")
    print("\n_________________________________________________________________________________________________________________________||")
