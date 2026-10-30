# number=[12,45,7,23,45,89,12,34,5,67]
# # 1
# print(number)

# # 2
# print(number[1])
# print(number[-1])

# # 3
# print(f"total number of elements: {len(number)}")
# from functools import reduce
# # 4
# print(f"Sum of all elements:{sum(number)}")

# sum=0
# for n in number:
#     sum+=n
# print(f"sum of number list elements :{sum}")

# sum1=reduce(lambda a,b:a+b,number)

# print(f"sum by using lambda and reduce :{sum1}")

# # 5

# print(f"max number :{max(number)}")
# print(f"min number :{min(number)}")

# max=0
# for n in number:
#     if max<n:
#         max=n
# print(f"max number by for loop :{max}")

# min=number[1]
# for n in number:
#     if min>n:
#         min=n
# print(f"min number by for loop :{min}")

# # 6
# print("all even numbers:")
# for n in number:
#     if n%2==0:
#         print(f"even:{n}")

# # 7

# print("all odd numbers :")
# for n in number:
#     if n%2!=0:
#         print(f"odd:{n}")
# # 8
# even=0
# odd=0
# for n in number:
#     if n % 2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"even count:{even}")
# print(f"odd count:{odd}")

# 5 bubble sort
# number=[12,45,7,23,45,89,12,34,5,67]
# for i in range(len(number)):
#     for j in range(len(number)):
#         if number[i]<number[j]:
#             minn=number[j]
#             number[j]=number[i]
#             number[i]=minn
#         # number[i],number[j]=min,number[i]
# print(number)
# print(f"max number :{number[-1]} and min number:{number[-1]}"

# )

# task 9
# wherethere 23 exits in the list

number=[12,45,7,23,45,89,12,34,5,67]

if 23 in number:
    print("23 exits in list")
else:
    print("not exits in list")

# 10:- index position
ind=number.index(89)
print(ind)

# 11
number.append(100)
print(number)

# 12
# import deque from collections
number.insert(3,50)
print(number)

ls=[1,2,5]

# 13


