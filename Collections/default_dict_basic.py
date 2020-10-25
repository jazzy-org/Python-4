#It is a subclass of the dict class that returns a dictionary like-object.
#The functionality of both dictionaries and defaultdict are almost same except it never raises a keyerror it provides the deafult value for the key that doesnot exixts.
from collections import defaultdict
def value():
	return "No"

d1 = defaultdict(value)
d1["deafult"] = 1
d1["dict"] = 2
print(d1["deafult"])  # 1
print(d1["dict"])  # 2
print(d1["defaultdict"]) # No

#instead of writing it in function we can use lambda parameter
d2 = defaultdict(lambda:"No")
d1["deafult"] = 1
d1["dict"] = 2
print(d1["deafult"])  # 1
print(d1["dict"])  # 2
print(d1["defaultdict"]) # No

#using list as default factory
#when the list class is passed as the argument then a default divt is created with the values that are list
d3 = defaultdict(list)
for i in range(5):
	d3[i].append(i)
print(d3)  #{0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})

#using int as default factory
#when the int class is passed then a defaultdict is created with default as zero.
d4 = defaultdict(int)
nums = [1,2,3,4,1,4,3,5]
for num in nums:
	d4[i] += 1
print(d4)  #{1: 2, 2: 1, 3: 2, 4: 2, 5: 1})




