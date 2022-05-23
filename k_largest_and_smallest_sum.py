k=int(input("enter your number: "))
n=int(input("enter your number: "))
l=[]
for i in range(0,n):
    num= int(input("enter your number: "))
    l.append(num)
def sum_of_numbers  (l,n,k) :
    l.sort() 
    if l[k-1]==l[-k]:
        a=l[k]**2
        return a
    else:
        s=l[k-1]+l[-k]
    return s
result = sum_of_numbers(l, n, k)
print(result)