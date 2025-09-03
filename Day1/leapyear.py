def leapornot(a):
    if(a%4==0 and a%100!=0):
        print(f'{a} is leap year')
    if(a%100==0 and a%400==0):
        print(f'{a} is a leap year')
    else:
        print(f'{a} is not a leap year')
a=int(input())
leapornot(a)