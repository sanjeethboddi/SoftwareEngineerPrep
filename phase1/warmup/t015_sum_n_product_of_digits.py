def sum_and_product_of_digits(num:int):
    sum_result = 0
    product_result = 1
    while num:
        sum_result += num%10
        product_result *= num%10
        num //=10
    
    return (sum_result, product_result)

num = 1234
sum_result, product_result = sum_and_product_of_digits(num)
print(sum_result, product_result)

num = 4825
sum_result, product_result = sum_and_product_of_digits(num)
print(sum_result, product_result)