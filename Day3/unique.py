def unique(list):
    freq={}
    for i in list:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for i in freq:
        if freq[i]==1:
            print(i,end=" ")
list=[1,2,3,1,2,35,67,8,7,8]
unique(list)
