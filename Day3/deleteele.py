def deleteelement(x,list):
    for i in range(x,len(list)-1):
        list[i]=list[i+1]
    list=list[:-1]
    print('after deleting an element: ',list)
list=[1,2,3,4,56]
deleteelement(1,list)




