def string_clean(s):
    i=0
    a=""
    while i<len(s):
        if  s[i].isdigit():
            pass
        else:
            a=a+s[i]
        i=i+1
    return a
print(string_clean("wertyui12345!@#$"))
