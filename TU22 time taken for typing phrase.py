import datetime
print("Type the following phrase:\nthe lazy fox jumped over the brown dog")
input("press enter when you are ready")
start = datetime.datetime.now()
while True:
    if input("") == "the lazy fox jumped over the brown dog":
        end = datetime.datetime.now()
        break
    else:
        print("wrong phrase")

print("It took you", (end - start).seconds + (end - start).microseconds/1000000, 'seconds')
