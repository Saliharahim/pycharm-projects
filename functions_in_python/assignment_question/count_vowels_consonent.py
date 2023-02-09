word=input("enter a word")
def count(word):
    w=0
    c=0
    v=["a","e","i","o","u","A","E","I","O","U"]
    for i in word:
        if i in v:
            w=w+1
        else:
            c=c+1
    print("consonent",c)
    print("vowels",w)
count(word)