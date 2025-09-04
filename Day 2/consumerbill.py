def amount(un):
    am=0.0
    if un<=50:
        am=un*3.80
    elif un<=100:
        am=50*3.80+(un-50)*4.20
    elif un<=200:
        am=50*3.80+50*4.20+(un-100)*5.10
    elif un<=300:
        am=50*3.80+50*4.20+100*5.10+(un-200)*6.30
    else:
        am=50*3.80+50*4.20+100*5.10+100*6.30+(un-300)*7.50
    return am
x=amount(150)
print(x)