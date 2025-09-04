def isprime(n):
    if n==2 or n==3:
        return True
    if n<=1:
        return False
    i=2
    while i<=n//2:
        if n%i==0:
            return False
        i=i+1
    return True
def primefactor(n):
    for i in range(1,n):
        if(n%i==0) and isprime(i):
            print(i)
primefactor(28)
