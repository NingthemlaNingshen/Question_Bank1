# a=" A coder in Navgurukul (park min lee) "
# a=" A coder (in Navgurukul) park min lee "
# i=0
# x=a.split()
# while i<len(x)-1:
#     i=i+1
#     if "(" in x[i] or ")" in x[i]:
#         continue
#     print(x[i],end=" ")
    # i=i+1
# a="McClane john"
# x=a.split()
# i=1
# s=""
# while i<=len(x):
#     s=s+" "+str(x[-i])
#     i=i+1
# print(s)


    # x=str.split()
    # i=1
    # s=""
    # while i<=len(x):
    #     s=s+str(x[-i])
    #     i=i+1
    # return s
# s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# n=int(input())
# for i in range(len(s)//n):
#     for j in range(n):
#         print(s[j],end="")
#     print()


n=int(input())
for i in range(n):
    for j in range(i):
        print("$",end="")
    print()
