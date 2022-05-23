s="1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 8 4 3 1 9 5 6 2"
i=0
l=[]
while i<len(s):
    if s[i] not in l:
        l.append(s[i])
    i=i+1
j=0
while j<len(l):
    k=0
    c=0
    while k<len(s):
        if l[j]== s[k]:
            c=c+1
        k=k+1
    if c==1:
        print(l[j])
    j=j+1

