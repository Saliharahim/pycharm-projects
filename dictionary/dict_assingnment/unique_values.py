listofdict=[{"v":"s001"},{"v":"s002"},{"v1":"s005"},{"v11":"s005"}]
setof_uvalues=set()
for i in listofdict:
    for values in i.values():
        #print(values)
        setof_uvalues.add(values)
print(setof_uvalues)
#OR
# ul=[]
# for i in listofdict:
#     ul.extend(list(i.values()))
# ul=set(ul)
# print(ul)