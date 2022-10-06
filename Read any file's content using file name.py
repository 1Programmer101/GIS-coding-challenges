File_name = input("Please enter the file name along with '.filetype' :\n")
with open(File_name, 'r') as file:
    print("Type 'n' when you would like to go to next line")
    for line in file:
        while input() != 'n':
            pass
        print(line, end="")
