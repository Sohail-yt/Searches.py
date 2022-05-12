def line(a,e):
    for i in range(len(a)):
        if e == a[i]:
            return i
a=[4,8,5,7,2,24,6,7,8721]
e=8721
print(line(a,e))