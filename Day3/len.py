def length(st):
    x=0
    for i in st:
        x=x+1
    return x

def compare(st1,st2):
    print(st1==st2)

def concatenate(st1,st2):
    st1=st1+st2
    print('after concatenation: ',st1)
    
st1="hi hello"
st2="welcome"
print(length(st1))
print(length(st2))
compare(st1,st2)
concatenate(st1,st2)
