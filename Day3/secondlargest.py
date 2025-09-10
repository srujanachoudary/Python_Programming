def secondlargest(li):
    fl=li[0]
    sl=fl
    for i in li:
        if fl<i:
            sl=fl
            fl=i
        if fl>i and sl<i:
            sl=i
    return sl
li=[1,222,3,455,66]
x=secondlargest(li)
print('second largest: ',x)
        