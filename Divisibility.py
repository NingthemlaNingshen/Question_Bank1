def divisibility():
    n=int(input("enter the len or size of your list: "))
    i=0
    l=[]
    while i<n:
        array=int(input("enter your number: "))
        l.append(str(array))
        i=i+1
    j=0
    s=""
    while j<len(l):
        s=s+l[j][-1]
        j=j+1
    if int(s)%10==0:
        return "Yes"
    else:
        return "No"
print(divisibility())