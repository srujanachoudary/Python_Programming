def printhighest(student):
    m=0
    mn=0
    for i in range(len(student)):
        if student[i][2]>m:
            m=student[i][2]
            mn=i
    print('highest marks is scored by ',student[mn][1])

def printmorethan75(student):
    for i in range(len(student)):
        if student[i][2]>75:
            print(f"{student[i][0]}  {student[i][1]} {student[i][2]}")
student=[('5b5','SRUJANA',89),('5b0','spandana',95),('584','Madhurika',78)]
printhighest(student)
printmorethan75(student)