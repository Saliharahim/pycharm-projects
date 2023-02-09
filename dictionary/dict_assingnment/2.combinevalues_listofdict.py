listofdict=[{"items":"item1","amount":400},{"items":"item2","amount":300},{"items":"item1","amount":750}]

lst={}
for i in listofdict:
    #print(i)
    if i['items'] not in lst:
        lst[i['items']]=i['amount']
    else:
        lst[i['items']] += i['amount']
print(lst)