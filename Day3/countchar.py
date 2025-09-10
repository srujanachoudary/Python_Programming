def countchar(x,str):
    count=0
    for i in range(len(str)):
        if str[i]==x:
            print(i,end=" ")

str="This is AI & DS training."
countchar('i',str)