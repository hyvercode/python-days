#if
x = 10

if x > 5:
    print("x lebih besar dari 5")


#if-else
x = 10

if x > 15:
    print("x lebih besar dari 15")
else:
    print("x tidak lebih besar dari 15")

#if-elif-else
x = 10

if x > 15:
    print("x lebih besar dari 15")
elif x == 10:
    print("x sama dengan 10")
else:
    print("x lebih kecil dari 10")

#for
# Iterasi dengan list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterasi dengan range
for i in range(5):
    print("Angka:", i)

#while
x = 0

while x < 5:
    print("Nilai x:", x)
    x += 1

#break
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#pass
for i in range(5):
    if i == 3:
        pass  # Tidak melakukan apa-apa
    print(i)

#case
num = 29

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} bukan bilangan prima")
            break
    else:
        print(f"{num} adalah bilangan prima")
else:
    print(f"{num} bukan bilangan prima")