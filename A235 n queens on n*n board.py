Queen_placed = []
any_arrangement = False
n = int(input("Enter the number n of queens u want to place on n*n board:"))

def is_crossing(q_spot):
    for elem in Queen_placed:
        if elem[0] == q_spot[0] or elem[1] == q_spot[1]:
            return True
        for diagonal in range(n):
            if elem[0] + diagonal == q_spot[0] and elem[1] + diagonal == q_spot[1]:
                return True
            if elem[0] - diagonal == q_spot[0] and elem[1] - diagonal == q_spot[1]:
                return True
            if elem[0] + diagonal == q_spot[0] and elem[1] - diagonal == q_spot[1]:
                return True
            if elem[0] - diagonal == q_spot[0] and elem[1] + diagonal == q_spot[1]:
                return True
    return False


def output_table(list_):
    array = [[0 for x in range(n)] for y in range(n)]
    for elem in list_:
        array[elem[0]][elem[1]] = 1
    for elems in array:
        for numbers in elems:
            print(numbers, end = " ")
        print("")
    print("-------------------")


# for row1 in range(n):
#     Queen_placed.append([0, row1])
#     for row in range(1, n):
#         for col in range(n):
#             if not is_crossing([row, col]):
#                 Queen_placed.append([row, col])
#                 break
#     print(Queen_placed)
#     if len(Queen_placed) >= n:
#         output_table(Queen_placed)
#         any_arrangement = True
#     # output_table(Queen_placed)
#     Queen_placed.clear()


def iterate(row_num):
    global any_arrangement
    if row_num + 1 < n:
        for col in range(n):
            if not is_crossing([row_num, col]):
                Queen_placed.append([row_num, col])
                iterate(row_num + 1)
                Queen_placed.pop()


    else:
        for col in range(n):
            if not is_crossing([row_num, col]):
                Queen_placed.append([row_num, col])
                if len(Queen_placed) == n:
                    output_table(Queen_placed)
                    any_arrangement = True



iterate(0)

if not any_arrangement:
    print("There is no way of arranging")
