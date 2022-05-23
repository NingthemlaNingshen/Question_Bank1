num=int(input("enter your number: "))
div=int(input("enter your number: "))
def sum_of_remainders():
    sum=0
    i=1
    while i<num:
        sum=i%div+sum
        i=i+1
    return sum
print(sum_of_remainders())
