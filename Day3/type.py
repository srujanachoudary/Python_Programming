def count(str):
    alphacount=0
    digitcount=0
    specialcount=0
    for i in str:
        if i.isalpha():
            alphacount+=1
        elif i.isdigit():
            digitcount+=1
        else:
            specialcount+=1
    print('no of alphabets are ',alphacount)
    print('no of digits are ',digitcount)
    print('no of special characters are: ',specialcount)
str="abcd123@#$%qsrt"
count(str)