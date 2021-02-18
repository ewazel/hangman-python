def bin_to_dec(bin_num):
    x = [int(i) for i in str(bin_num)]
    x.reverse()

    dec = 0
    a = 0

    for i in x:
        c = i * (2 ** a)
        a += 1
        dec += c

    print(f"{bin_num} = {dec}")

# bin_to_dec(1001100110)

def dec_to_bin(dec_num):
    x = dec_num
    div = 0
    mod = 0
    bin = []

    while x > 0:
        div = x / 2
        mod = x % 2
        bin.append(mod)
        x = int(div)

    bin.reverse()
    bin_str = ("".join(map(str, bin)))
    print(f"{dec_num} = {bin_str}")

# dec_to_bin(16)

def main():
    user_input = input("Do you want to convert binary or decimal number? B / D ")
    user_number = int(input("Please, write a number: "))

    if user_input.lower() == "b":
        bin_to_dec(user_number)
    elif user_input.lower() == "d":
        dec_to_bin(user_number)

    user_input = input("Write 'y' if you want to convert another number. ")

    if user_input.lower() == "y":
        main()

main()