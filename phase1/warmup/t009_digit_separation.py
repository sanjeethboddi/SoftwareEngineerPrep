def separate_digits_string_way(a:int):
    print(" ".join(list(str(a))))

def separate_digits_math_way(a:int):
    # 2 pass 
    digits_counter = 0
    x = a
    while x:
        x//=10
        digits_counter += 1

    while digits_counter:
        print(a//10**(digits_counter-1), end=" ")
        a%=10**(digits_counter-1)
        digits_counter -= 1
    print()


separate_digits_math_way(1233244)
separate_digits_string_way(43598)
        