def charoralphaodigit(c):
    if c.isalpha():
        print(f'{c} is an alphabet')
    elif c.isdigit():
        print(f'{c} is a digit')
    else:
        print(f'{c} is a special character')
c=input('Enter a character')
charoralphaodigit(c)