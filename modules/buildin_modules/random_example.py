import random
#print(dir(random))
y=random.random()
print(y)

x= random.randint(1,9)
print(x)

d=random.randrange(1,100,2)
print(d)

#c=random.choice('computer')
#print(c)

c=random.choice('134256')
print(c)

numbers=[1,2,3,4,5,6]
random.shuffle(numbers)
print(numbers)
