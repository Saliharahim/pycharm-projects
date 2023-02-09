f= open('test','r')
#print(f.read())

#print(f.read(20))# starting and ending count cheyyum,,

# print(f.readline())#  use for read line by line
# print(f.readline())

''' also we can use for loop for read a line'''
# for i in f:
#    print(i)

f.close()# for close the file after  operations done

# f=open('test','a')
# f.write('python is a oop')
#
# f.close()

# f=open('test','r')
# print(f.read())
# f.close()

# f=open('test','w')
# f.write('python is a oop')
# f.close()
#
# f=open('test','r')
# print(f.read())
# f.close()

''' seek()= it sets the current file positioning'''

# f=open('test','r')
# f.seek(7)
# print(f.readline())
# f.close()

''' tell()==returns the current position of file'''
# f=open('test','r')
# f.readline()
# pos=f.tell()
# f.close()
# print('position is :',pos)

# problem=WAP to read a file line by line and sttire it into a list
# def file_read(fna):
#     with open(fna) as f:  # this is equal to open as read mode and we dont have to close this ,it will automatically close aakum
#         output=f.readlines() # it returns list
#         print(output)
# file_read('test')

# from shutil import copyfile
# copyfile('test','test2')

# Question
# str='cat mat rat cat pat sat cat rat mat pat rat'
# s=str.split(' ')
# print(s)
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

''' using a file'''

f=open('string_prgm_ex','r')
dict={}
for i in f:
    var=i.split(' ')
    for j in var:
        if j not in dict:
            dict[j]=1
        else:
            dict[j]+=1
print(dict)