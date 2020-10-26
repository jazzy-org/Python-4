#It is a dictionary subclass that remembers the order that keys we re first inserted.
from collections import OrderDict
od1 = OrderDict()
od1['a'] = 1
od1['b'] =2
od1['c'] = 3
od1['d'] = 4
for key,value in od1.items():
	print(key,value)

#answer
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 4)

# if the value of a certain key is changed the position of the key remain unchanged
od2 = OrderDict()
od2['a'] = 1
od2['b'] =2
od2['c'] = 3
od2['d'] = 4
for key,value in od2.items():
	print(key,value)
#answer
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 4)
od2['c'] = 5
for key,value in od2.items():
	print(key,value)
#answer
# ('a', 1)
# ('b', 2)
# ('c', 5)
# ('d', 4)

# Deleting and reinserting the same key will push it to the back as orderdict however maintains the order of insertion
# It can be used as a stack with the help of popitem function.