#     repeated elements to '$'
str1="restart"
str2=[]
for i in str1:
    a=str1[0]
    if a==i:
        str2=str1[1:].replace(i,'$')
print(a+str2)
print(str1[1:])

#return length of the longest word
# words=['saliha','duaa','shamnas','sajna']
# length=max(words)
# print(length,len(length ))
