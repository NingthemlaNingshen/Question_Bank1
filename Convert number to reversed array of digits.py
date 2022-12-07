def Convert(n):
    s=str(n)
    l=[]
    i=1
    while i<=len(s):
        l.append(int(s[-i]))
        i=i+1
    return l
print(Convert(234567))  ##to convert into reversed list
