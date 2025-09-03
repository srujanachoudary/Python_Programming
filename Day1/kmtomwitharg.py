def YearMonth(d):
    y=d/365
    m=y*12
    print("years:",round(y,1))
    print('months:',round(m,1))
x=int(input())
YearMonth(x)