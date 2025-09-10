def oddeven(li):
    oddcount=0
    evencount=0
    for n in li:
        if n%2==1:
            oddcount+=1
        else:
            evencount+=1
    print('odd count= ',oddcount,'even count= ',evencount)
li=[1,2,3,4,5,6,7,8,9]
oddeven(li)