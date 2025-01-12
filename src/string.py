#String

name="Roger"

print(name)

fullname = "Jhone" + " Age 23"

print(fullname)


name = "Jhon"
name += "Age 23"
print(name) #Jhon Age 23

print(name)

#Convert number to string
print("Jhon is " + str(8) + " years old") #Jhon is 8 years old


print("""Jhon is
    8
years old
""")
#double quotes, or single quotes
print('''
Jhon is
8
years old
''')

#lower case
name = "Jhon"
print(name.lower()) #"jhon"

#len
name = "Jhon"
print(len(name)) #5

#in
name = "Jhon"
print("hon" in name) #True