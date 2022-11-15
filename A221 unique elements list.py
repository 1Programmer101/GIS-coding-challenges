def remove_duplicates(list1):
    list2 = []
    for elem in list1:
        if elem not in list2:
            list2.append(elem)
    return list2
