def count(str):
    vowels="aeiouAEIOU"
    vcount=0
    ccount=0
    for i in str:
        if i.isalpha():
            if i in vowels:
                vcount+=1
            else:
                ccount+=1
    print('vowels: ',vcount)
    print('consonants: ',ccount)
str="aewqrst123"
count(str)