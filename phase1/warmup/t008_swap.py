def swap_pythonic_way(a,b):
    return b,a 

def swap_math_way(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b 
    
a,b = 10,5
a,b = swap_pythonic_way(a,b)
print(a,b)

c,d = 10,5
c,d = swap_math_way(c,d)
print(c,d)