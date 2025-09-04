def numberofdig(n):
    count=0
    for i in str(n):
        count=count+1
    return count
print(numberofdig(123456))