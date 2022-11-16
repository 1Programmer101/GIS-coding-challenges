roman_vals = {'M' : 1000,
              'CM' : 900,
              'D' : 500,
              'CD' : 400,
              'C' : 100,
              'XC' : 90,
              'L' : 50,
              'XL' : 40,
              'X' : 10,
              'IX' : 9,
              'V' : 5,
              'IV' : 4,
              'I' : 1}


def get_key(val):
    for key, value in roman_vals.items():
        if val == value:
            return key


def num_to_rom(num):
    index_ = 0
    amount_left = num
    roman_numeral_l = []
    while amount_left != 0:
        dec_num_of_rom = list(roman_vals.values())[index_]
        if amount_left >= dec_num_of_rom:
            roman_numeral_l.append(get_key(dec_num_of_rom))
            amount_left = amount_left - dec_num_of_rom
        else:
            index_ += 1
    return "".join(roman_numeral_l)


def rom_to_num(roman):
    for x in range(1, 4000):
        if num_to_rom(x) == roman:
            return x


num = input("Enter number to be converted to roman numeral. (If roman numeral to be converted press enter)\n")
roman_num = False
if num == "":
    roman_num = input("Enter roman numeral:\n")
    num = False

if not num:
    print(rom_to_num(roman_num))
if not roman_num:
    print(num_to_rom(int(num)))
