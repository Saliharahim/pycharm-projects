#century year divided by 400 is leap year
year=int(input("enter a year"))
if (year%100==0) and (year%400==0):
    print("leap year")
elif(year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not leap year")