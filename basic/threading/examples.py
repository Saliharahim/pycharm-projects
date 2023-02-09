# sleep
from time import sleep
# def tash():
#     #block for a moment
#     sleep(3)
#     # dislplay a message
#     print("hello")
# tash()
# single threading
# call using thread
from time import sleep
# def tash():
#     #block for a moment
#     sleep(3)
#     # dislplay a message
#     print("hello")
# from threading import Thread
# thread=Thread(target=tash)
# thread.start()

# passing arguments
# from time import sleep
# def tash(sleep_time,message):
#     #block for a moment
#     sleep(sleep_time)
#     # dislplay a message
#     print(message)
# from threading import Thread
# thread=Thread(target=tash,args=(1.5,'hello'))
# thread.start() #run the thread
# #waiting for the thraed to finish
# print("waiting for the thread..")
# thread.join()

# multithreading
# import time
# import threading
# def cal_sqre(num):
#     print("calculate the sqaure of the number")
#     for i in num:
#         time.sleep(0.3)
#         print("sqaure:",i*i)
# def cal_cube(num):
#     print("calculate the cube of given number")
#     for i in num:
#         time.sleep(0.3)
#         print("cube:",i*i*i)
# arr=[4,5,6,7,2]
# t1=time.time()
# cal_sqre(arr)
# cal_cube(arr)

# using threading
import time
import threading
def cal_sqre(num):
    print("calculate the sqaure of the number")
    for i in num:
        time.sleep(0.3)
        print("sqaure:",i*i)
def cal_cube(num):
    print("calculate the cube of given number")
    for i in num:
        time.sleep(0.3)
        print("cube:",i*i*i)
arr=[4,5,6,7,2]
t1=time.time()
# cal_sqre(arr)
# cal_cube(arr)
th1=threading.Thread(target=cal_sqre,args=(arr,))
th2=threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by thraeds is:",time.time()-t1)
