def strongnum(n):
    for i in range(1,n+1):
        x=i
        sum=0
        while x>0:
            rem=x%10
            fact=1
            for k in range(1,rem+1):
                fact=fact*k
            sum=sum+fact
            x=x//10
        if(sum==i):
            print(i,end=" ")
strongnum(1000)
