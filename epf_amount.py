
# def epf_amount():
#     epf_principle=int(input("enter your number: "))
#     year=int(input("enter the year:"))
#     user=input("Did the employee retired or Quits?? ")
#     if user=="retired":
#         print("The employee retired")
#         print("The total epf_amount is: ",1.2*epf_principle*year)
#     else:
#         print("The employee Quits")
#         if year<5:
#             print("Cannot withdraw any money")
#         elif year>5:
#             if year<10:
#                 print("epf_amount: ",0.9*epf_principle*year)
#             elif year<20:
#                 print("epf_amount: ",1*epf_principle*year)
#             else:
#                 print("The total epf_amount is: ",1.2*epf_principle*year)
# epf_amount()


# name = "geeks FOR grace"
# x = name.title()
# print(x)

# def solve(s):
#     for i in s.split():
#         s=s.replace(i,i.capitalize())
#     return s  

# n=5
# i=0
# while i<5:
#     print(str(i)*i)
#     i=i+1

# name1 = "geeks"
# name2 = "for"
# name3 = "geeks"
# print(name1.capitalize() + name2.capitalize()
# #                          + name3.capitalize())
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
    # print(sorted(list(set(arr)))[-2]) 


# n="eerty"
# c=0
# i=0
# while i<len(n):
#     j=0
#     c=0
#     while j<len(n):
#         if n[i]==n[j]:
#             c=c+1
#         j=j+1
#     i=i+1
# print(c)

# l2=[10,9,87,6,5,67]
# l2.sort()
# print(l2)
# l=[]
# l1=[]
# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         l=l+[[name,score]]
#         l1=l1+[score]
# x=sorted(set(l1))[1]
# for n,s in sorted(l):
#     if s==x:
#         print(n)
# print(l)
# print(x)

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
