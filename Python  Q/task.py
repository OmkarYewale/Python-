number = [12,45,7,23,45,89,12,34,5,67]
# task 1
for n in number:
    print(n)

# task 2
print(number[1])

print(number[-1])

# task 3

print("toatal number of elements :",len(number))

# task 4

sum=0

for n in number:
    sum=n+sum

print(f"sum of all elements {sum}")

# task 5

max_number = max(number)

print("max number",max_number)

small_num = min(number)

print(f"small number {small_num}")

# task 6

for n in number:
    if n % 2 == 0:
        print(n)

# task 7
for n in number:
    if n % 2 != 0:
        print(n)

# task 8

even_count = 0
for n in number:
    if n % 2 == 0:
        even_count +=1

print(f"even count is {even_count}")

odd_count = 0
for n in number:
    if n % 2 != 0:
        odd_count +=1
print(f"odd count is {odd_count}")

# task 9

if 23 in number:
    print("23 is prasent in numer list")
else:
    print("not prasent")

# task 10

print(f" index position of 89 is {number.index(89)}")

# task 11

number.append(100)

print(number)

# task 12

number.insert(3,50)
print(number)

# task 13

number.remove()

print(number)

# task 14

remove_dupli =set(number)

print(remove_dupli)

# task 15

sort_list_ascen =number.sort()

sort_list_descen = sort_list_ascen[::-1]



# task 16

square = []
for n in number:
    square.append(n*n)

# task 17

grater=[]

for n in number:
    if n >30:
        grater.append(n)

print(grater)

# task 18

for n in number[::-1]:
    print(n)

# task 19

print(f"second largest {sort_list_ascen[::-1]}")

# task 20
print(f"second samllest {sort_list_ascen[2]}")

# task 21

for n in number:
    print(f"")


