def maximum(d,i):
    max=0
    for key in d:
        a=key
        x=d[key][i]
        if x>max:
            max=x
            z=a
    # return max      ## for marks
    return z          ##for names
def names(d):
    i=0
    while i<len(d):
        y=maximum(d,i)
        print(y)
        i=i+1
d={"nim":[10,45,38],"tim":[31,21,7],"kim":[15,34,40]}
names(d)