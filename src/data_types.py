name="Jhon"

name = "Jhon"
type(name) == str #True
print(type(name) == str )


name = "Jhon"
result = isinstance(name, str) #True

print("variable name is string ? ",result)

#contoh int dan float
age = 1
print(type(age) == int) #True

fraction = 0.1 
print(type(fraction) == float) #True

#boolean

bool_1=True
bool_2=False


print("Bool 1",bool_1,"Bool 2",bool_2)

#none or null

data=None

print("None ", data)

#list
list_1=[1,2,3,4,5,6,7]

print("List 1",list_1)
print("List 1 index 0 is ",list_1[0])

# list with str as element's data type
list_2 = ["grayson", "jason", "tim", "damian"]
print("List 2",list_2)
print("List 2 index 1 is ",list_2[2])

# list with various data type in the element
list_3 = [24, False, "Hello Python"]
print("List 3",list_3)
print("List 3 index 2 is ",list_3[2])

#Tuple
# tuple with int as element's data type
tuple_1 = (2, 3, 4)
print("Tuple 1",tuple_1)
print("Tuple 1 index 0 is ",tuple_1[0])
# tuple with str as element's data type
tuple_2 = ("numenor", "valinor")
print("Tuple 2",tuple_2)
print("Tuple 2 index 1 is ",tuple_2[1])
# tuple with various data type in the element
tuple_3 = (24, False, "Hello Python")
print("Tuple 3",tuple_3)
print("Tuple 3 index 1 is ",tuple_3[1])

# Dictionary
 
profile_1 = { "name": "Noval", "hobbies": ["gaming", "learning"] }

print("name: %s" % (profile_1["name"]))

print("hobbies: %s" % (profile_1["hobbies"]))

#Set

set_1 = {"pineapple", "spaghetti"} 
print(set_1)