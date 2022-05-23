t = int(input("enter your rangr: "))
while t:
    c,d,l = map(int,input().split())
    total = (c+d)*4
    mini = max(0,c-d*2)
    print(mini)
    if(total>=l and l%4==0 and (d+mini)*4<=l):
        print("yes")
    else:
        print("no")
    t-=1

##or 

t=int(input("enter your range: "))
for i in range(t):
    C,D,L=map(int,input().split())
    l=4*(C+D)
    l1=max(0,C-D*2)
    if l>=L and L%4==0 and (D+l1)*4<=L:
        print("Yes")
    else:
        print("No")
