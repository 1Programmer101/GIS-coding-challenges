def NAND(a,b):
    return not (a and b)


def AND(a, b):
    l1 = NAND(a, b)
    return NAND(l1, l1)


def OR(a, b):
    l1 = NAND(a, a)
    l2 = NAND(b, b)
    return NAND(l1, l2)


def NOR(a, b):
    or_gate = OR(a, b)
    return NAND(or_gate, or_gate)


def NOT(a):
    return NAND(a, a)


def XOR(a, b):
    l1 = NAND(a, b)
    l2 = NAND(a, l1)
    l3 = NAND(b, l1)
    return NAND(l2, l3)



