def amountofnotes(am):
    count=0
    if am>=2000:
        count=count+am//2000
        am=am-(am//2000)*2000
    if am>=500:
        count=count+am//500
        am=am-(am//500)*500
    if am>=100:
        count=count+am//100
        am=am-(am//100)*100
    if am>=50:
        count=count+am//50
        am=am-(am//50)*50
    if am>=10:
        count=count+am//10
        am=am-(am//10)*10
    return count
print(amountofnotes(15000))