word=input("enter a word")
count=0
for i in word:
    freq=word.count(i)
    print({str(i)+":"+str(freq)},end=" ")
