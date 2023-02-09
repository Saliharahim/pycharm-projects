r=int(input("enter row"))
for i in range(0,r):
      for j in range(i+1):
          print(j+1,end=" ")
      print()
#
# 2.
# r=int(input("enter row"))
# for i in range(r+1,1,-1):
#     for j in range(i-1,0,-1):
#        print(j,end=" ")
#    print()
# 3. FULL PYRAMID
# n=5
# for i in range(n):
#     for s in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#4.reverse pattern 10-1
# n=10
# for i in range(0,n):
#     for j in range(n-i,0,-1):
#         print(j,end=" ")
#     print()
