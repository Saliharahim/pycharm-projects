# Python3 code to demonstrate working of
# Concatenate Similar Key values
# Using loop

# initializing list
test_list = [{'gfg': [1, 5, 6, 7], 'good': [9, 6, 2, 10],
			'CS': [4, 5, 6]},
			{'gfg': [5, 6, 7, 8], 'CS': [5, 7, 10]},
			{'gfg': [7, 5], 'best': [5, 7]}]

# printing original list
print("The original list is : " + str(test_list))

# Concatenate Similar Key values
# Using loop
res = dict1()
for dict1 in test_list:
	print(dict)
	for list in dict1:
		print(list)
		if list in res:
			res[list] += (dict1[list])
			#print("res",res[list])
		else:
			res[list] = dict1[list]

# printing result
print("The concatenated dictionary : " + str(res))
