def total_marks(d,i):
    sum=0
    for key in d:
        sum+=d[key][i]
    return sum
def all_mark(d,i):
    i=0
    while i<len(d):
        x=total_marks(d, i)
        print(x)
        i=i+1
d={"nim":[10,45,38],"tim":[31,21,7],"kim":[15,34,40]}
i=0
all_mark(d,i)    