def removeduplicate(list):
    freq={}
    result=[0]*len(list)
    j=0
    for i in list:
        if i not in freq:
            freq[i]=1
            result[j]=i
            j+=1
        else:
            continue
    result=result[:j]
    print(result)
list=[1,1,2,2,3,4,55,5,4,6]
removeduplicate(list)