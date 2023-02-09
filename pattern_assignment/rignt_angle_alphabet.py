n=int(input("enter a number"))
#for i in range(65,91):
 #   print(chr(i),end=" ")
char=65
for i in range(n):
    for j in range(i+1):
        print(chr(char),end=" ")
        char=char+1
    print()




































