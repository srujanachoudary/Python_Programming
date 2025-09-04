def firstlast(n):
    l=n%10
    rem=0
    while n>0:
        rem=n%10
        n=n//10
    return rem,l
print(firstlast(456))