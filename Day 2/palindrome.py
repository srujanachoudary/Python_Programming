def palindrome(x):
    y=str(x)
    z=y[::-1]
    if(y==z):
        return True
    else:
        return False
n=int(input())
for i in range(n):
    if palindrome(i):
        print(i,end=" ")
