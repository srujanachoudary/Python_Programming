def grade(m):
    if m>=40:
        if m<50:
            print('C grade')
        elif m>50 and m<70:
            print('B grade')
        elif m>70 and m<80:
            print('A grade')
        else:
            print('Distinction')
    else:
        print('Fail')
m1,m2,m3=map(int,input('Enter the marks').split(" "))
grade(m1)
grade(m2)
grade(m3)
        