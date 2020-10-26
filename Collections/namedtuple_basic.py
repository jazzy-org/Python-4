#Like dictionaries it also contains keys that are hashed to a particular value.
#It supports both access from key value and iteration
from collections import namedtuple,col

nd1 = namedtuple('Student',['name','age','DOB'])
S = Student('suman','20','2612000')   
print ("The Student age using index is : ",end ="")   
print (S[1])
#The Student age using index is : 20
print ("The Student name using keyname is : ",end ="")   
print (S.name) 
#The Student name using keyname is : suman

#this can also be accessed using getattr
print ("The Student DOB using getattr() is : ",end ="") 
print (getattr(S,'DOB'))
#The Student DOB using getattr() is : 2612000

#some methods that can be used to convert other collections into namedtuple
nd2 = col.namedtuple('Employee',['name','city','salary'])
my_list = ['Suman','Bangalore','100000']
e1 = nd2._make(my_list)
print(e1)
#Employee(name='Asim', city='Delhi', salary='25000')

