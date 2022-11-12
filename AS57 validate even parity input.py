while True:
    byte = input("Input byte:")
    if len(byte) != 8:
        continue
    count = 0
    for digit in byte:
        if digit == '1':
            count += 1

    if count % 2 == 0:
        print("validated")
        break
    else:
        print("Not accepted. Not even parity")
