def frequency(list):
    freq={}
    for i in list:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for i in freq:
        print(f'{i}->{freq[i]}')
list=[1,2,31,2,34,5,6,6,6,6]
frequency(list)