def isPrime(n):
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
print(isPrime(98))