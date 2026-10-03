def divide(*args):
    if len(args) < 2:
        raise Exception("Insufficient Parameters")
    arg1 = args[0]
    try:
        for arg2 in args[1:]:
            arg1 /=arg2  
    except ZeroDivisionError as e:
        print("Bitch You can't divide with 0")
        raise e
    return arg1
print(divide(1,3,5))
print(divide(0,4,3))
# print(divide(1,2,0))
