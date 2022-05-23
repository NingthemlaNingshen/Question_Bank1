def average (d,i):
    sum=0
    for key in d:
        sum+=d[key][i]
    return sum/len(d[key])
def all_mark(d,i):
    while i<len(d):
        x=average(d,i)
        print(x)
        i=i+1
d={"nim":[10,45,38],"tim":[31,21,7],"kim":[15,34,40]}
i=0
all_mark(d,i)