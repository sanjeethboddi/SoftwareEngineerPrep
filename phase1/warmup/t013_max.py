def max_val(*nums)->int|float:
    result = -float('inf')
    for num in nums:
        if num > result:
            result = num
    return result

print(max_val(1,4,2,3,23,345,2,4,1234,31,3))
