def factorial(n):
    if n <=1:
        return 1

    result = n
    for i in range(n-1,1,-1):
        result *= i 
    return result

for i in range(10):
    print(i,factorial(i))

