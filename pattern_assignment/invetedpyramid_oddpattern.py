# n=int(input("enter a limit"))
# for i in range(n):
#     for s in range(i):
#         print("  ",end=" ")
#     for j in range(2*(n-i)-1):
#         print(" *",end=" ")
#     print()

#row=8
# for i in range(row):
#     for j in range(row - i):
#         print(' ', end='')  # printing space required and staying in same line
#
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == row-1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()  # printing new line

# for i in range(row, 0, -1):
#     for j in range(row - i):
#         print(' ', end='')  # printing space and staying in same line
#
#     for j in range(2 * i - 1):
#         if i==0 or i==j*2 or j==row-1:
#             print("*",end=" ")
#         print('*', end='')  # printing * and staying in same line
#     print()  # printing new line


n = 5
for i in range(n):
    for s in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

for i in range(n-1):
    for s in range(i+1):
        print(" ", end="")
    for j in range(2*(n-i-1) -1):
        print("*", end="")
    print()