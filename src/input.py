age = input("Please input your age : ")
str_age=None

if int(age) < 25:
    age="Young"
else:
    age="Old"
print("Your age is %s" % (age))

 
 
grade = int(input('Enter your current grade: '))
prev_grade = int(input('Enter your previous grade: '))
if grade >= 90 and prev_grade >= 65: 
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome. you definitely working hard, right?")
elif grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")
if (grade >= 65 and not prev_grade >= 65) or (not grade >= 65 and prev_grade >= 65):
    print("at least you passed one exam. good job!")

#one line 
if grade >= 65: print("passed the exam")
if grade < 65: print("below the passing grade")

#ternary
 
print("passed the exam") if grade >= 65 else print("below the passing grade")