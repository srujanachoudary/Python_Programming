def clean(day):
    set1=set(day)
    day=list(set1)

    for i in range(len(day)):
        x=day[i].lower()
        day.remove(day[i])
        day.insert(i,x)
    return day

def unique(day1,day2,day3):
    print(set(day1) | set(day2) |set(day3))

def displayfullpresent(day1,day2,day3):
    set1, set2, set3 = set(day1), set(day2), set(day3)
    print(' trainess who are full present',(set1 & set2 & set3))

def presentoneday(day1,day2,day3):
    set1, set2, set3 = set(day1), set(day2), set(day3)
    result = (set1 - set2 - set3) | (set2 - set1 - set3) | (set3 - set1 - set2)
    print('Trainees present exactly one day:', result)

def pairwisecount(day1,day2,day3):
    set1, set2, set3 = set(day1), set(day2), set(day3)
    print('day 1 and day 2: ',set1&set2)
    print('day 2 and day 3: ',set2&set3)
    print('day 1 and day 3: ',set1&set3)

    
day1=['A','b','c','d','e','f']
day2=['d','e','f','G','H','i','b']
day3=['g','h','i','J','K','L','a','b']
day1=clean(day1)
day2=clean(day2)
day3=clean(day3)
print('After cleaning')
print(day1)
print(day2)
print(day3)
unique(day1,day2,day3)
displayfullpresent(day1,day2,day3)
presentoneday(day1,day2,day3)
pairwisecount(day1,day2,day3)