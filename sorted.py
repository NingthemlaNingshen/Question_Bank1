l=[]
l1=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        l=l+[[name,score]]
        l1=l1+[score]
x=sorted(set(l1))[1]
for n,s in sorted(l):
    if s==x:
        print(n)
print(l)
print(x)

##or

l=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    l=l+[[name,score]]
i=0
s=[]
while i<len(l):
    s.append(l[i][1]) 
    i=i+1
s.sort()
x=s[1]
for j,k in sorted(l):
    if k==x:
        print(j)
