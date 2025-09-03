rno=input('Enter roll number:')
name=input("enter name:")
m1,m2,m3=map(int,input().split(","))
total=m1+m2+m3
average=total/3
print('Roll number: ',rno,"\n",'name: ',name,'\n','subject 1: ',m1,'\n','subject 2: ',m2,'\n','subject 3: ',m3)
print('total: ',total)
print('average: ',round(average,2))
