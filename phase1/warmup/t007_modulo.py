def modulo(a,b):
    return a%b 

def is_even(a:int)->bool:
    return modulo(a,2)==0

def is_divisible_by_9(a:int)->bool:
    return modulo(a,9)==0

print(is_even(5))
print(is_divisible_by_9(81))
