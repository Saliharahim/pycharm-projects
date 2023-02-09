# immutable,unordered,unindexed,duplicates not allow
# set is immutable, but it can be add or remove a item

set1={1,2,3,4,5}
print(set1)

set1.add(7)#   add single item
print(set1)

set1.remove(7)    #when we try to remove a item that not contain in set,python show a error
print(set1)

set2={1,2,3,"hello",(1,2,3)}
print(set2)
#for add a list in it we use set of list
a=set([1,2,3])
print(a)      # its datatype is set



#update
sa={1,2,3,4}
se={1,7,6,5}
sa.update(se)
print(sa)

#discard
sa.discard(7)
print(sa) #here when we remove a item that does inset,python does not show error


#pop== pop will delete a random item from the set,,unorederd item

#clear==it empty the set

se.clear()
print(se)

#copy==for create a copy

