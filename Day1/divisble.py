def divby5(x):
    return x%5==0
def divby11(x):
    return x%11==0
a=int(input())
if divby5(a) and divby11(a):
    print(f'{a} is divisible by 5 and 11')
