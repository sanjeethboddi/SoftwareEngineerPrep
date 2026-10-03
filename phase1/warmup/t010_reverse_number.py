def reverse_number(x:int):
    ans = 0
    while x:
        ans *= 10
        ans += x%10
        x//=10
    return ans
print(reverse_number(531240))
print(reverse_number(209345))
print(reverse_number(3242))


        
