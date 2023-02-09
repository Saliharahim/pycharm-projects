word=input("enter a word")
count=0
for i in word:
    freq=word.count(i)
    if freq==1:
        print(str(i)+":"+str(freq),end=" ""\n")
    else:
        print(str(i)+"   this letter is a repeating character")
   # print(str(i)+":"+str(freq),end=" ")
