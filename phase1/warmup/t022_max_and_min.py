def max_and_min(*nums):
    max_result = -float('inf')
    min_result = float('inf')

    for num in nums:
        if num > max_result:
            max_result = num
        if num < min_result:
            min_result = num

    return (max_result, min_result)


print(max_and_min(1,2,3,-3,-5,-9,139,-3,234,3,0,-33))