dict1={1:{"name":"saliha","age":21,"course":"python"},2:{"address":"ABC","firm":"cse"}}
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#change
dict1[1]["age"]=22
#print(dict1)
#UPDATE
dict1[2]["domain"]="python"
dict1[2]["year"]=2001
print(dict1)
#COPY
#print(dict1.copy())
#POP
#print(dict1.pop("age"))
dict1.update({2:{"name":"sali","place":"kochin"}})
print(dict1)