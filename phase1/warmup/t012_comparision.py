# check the comparators in other languages, or sorting, or etc. 
def compare(x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    else:
        return 0

x,y = 0,1
comparison_result = compare(x,y)
if comparison_result==0:
    print(f"{x}={y}")
elif comparison_result==-1:
    print(f"{x} < {y}")
else:
    print(f"{x} > {y}")


