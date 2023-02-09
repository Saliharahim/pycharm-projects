word=input("enter a word")
# if(word==word[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")
a=len(word)
s=0
while a>0:
    dig=a%10
    s=s+dig
    temp=a//10
if s==word:
    print("palindrom")
else:
    print("not palindrom")