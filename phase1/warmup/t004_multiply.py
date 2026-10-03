def multiply(*args):
    product = 1
    for i in args:
        product *= i
    return product
print(multiply(4,5,2))
