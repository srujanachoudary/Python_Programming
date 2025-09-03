cno=int(input('enter consumer number:'))
cname=input('enter consumer name:')
pmr=int(input("enter present month reading:"))
lmr=int(input("enter last month reading:"))
tu=pmr-lmr
cbill=tu*3.80
print('Consumer number: ',cno,'\n','Consumer name: ',cname,'\n','Present month reading: ',pmr,'\n','Last month reading: ',lmr,'\n','Total units: ',tu,'\n','Current bil: ',cbill,'\n')
messge=f"Consumer number: {cno}\n Consumer name: {cname}\n Present month reading: {pmr}\n Last month reading:{lmr}\n Total units: {tu}\n Current bil: {cbill}\n"
print(messge)
