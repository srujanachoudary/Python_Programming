def countoccurence(st):
    freq={}
    for i in st:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    res=""
    for i in freq:
        res+=i+str(freq[i])
    print(res)
st="aaabbbbccccdd"
countoccurence(st)