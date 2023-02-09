str1="lets google the pineapple"
str2=str1.split(" ")
# print(str2)
str3=[]
str4=[]
for i in str2:
    l=" "
    for j in i:
        if j in l:
            continue
        else:
            l=l+j
    str3.append(l)
    str4="".join(str3)  # or print(' '.join(str2))
print(str4)

