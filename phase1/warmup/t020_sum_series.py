
def sum_of_first_n_positive_nums_math_way(n):
    return (n*(n+1))//2

def sum_of_first_n_positive_nums_loop_way(n):
    sum_val = 0
    for i in range(1,n+1):
        sum_val += i
    return sum_val

def sum_of_evens_in_first_n_positive_nums_math_way(n):
    k=n//2
    return k*(k+1)

def sum_of_evens_in_first_n_positive_nums_loop_way(n):
    sum_val = 0
    for i in range(2,n+1,2):
        sum_val += i
    return sum_val



def sum_of_odds_in_first_n_positive_nums_math_way(n):
    k= n//2 if n%2==0 else (n+1)//2
    return k*k

def sum_of_odds_in_first_n_positive_nums_loop_way(n):
    sum_val = 0
    for i in range(1,n+1,2):
        sum_val += i
    return sum_val


for i in range(1, 11):
    print("sum_of_first_n_positive_nums", i, sum_of_first_n_positive_nums_math_way(i), sum_of_first_n_positive_nums_loop_way(i))

print("-"*50)

for i in range(1, 11):
    print("sum_of_evens_in_first_n_positive_nums", i, sum_of_evens_in_first_n_positive_nums_math_way(i), sum_of_evens_in_first_n_positive_nums_loop_way(i))

print("-"*50)

for i in range(1, 11):
    print("sum_of_odds_in_first_n_positive_nums", i, sum_of_odds_in_first_n_positive_nums_math_way(i), sum_of_odds_in_first_n_positive_nums_loop_way(i))

