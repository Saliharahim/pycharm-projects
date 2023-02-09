str1=["john","","jack","emma","","jins","lina"]
for i in str1:
    #print(i)
    if i=="":
        str1.remove(i)
print(str1)