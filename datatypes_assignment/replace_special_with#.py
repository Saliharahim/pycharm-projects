str1="/* is @ developer & musician!!"
change='/','*','@','&','!'
for char in change:
    str1=str1.replace(char,"#")
print(str1)