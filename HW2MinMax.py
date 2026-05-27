#Task :-> find second min and max
salary=[67000,45000,78000,55000,28000]
# #First method
# salary.sort()
# print(F"second min number ={salary[1]}")
# print(f"second max number={salary[-2]}")

#second method
temp=0
for i in range(0,len(salary)):
    min=salary[i]
    index=i
    for j in range(i+1,len(salary)):
        if min>salary[j]:
            min=salary[j]
            index=j
    temp=salary[i]
    salary[i]=min
    salary[index]=temp
print(salary)
print(F"second min salary ={salary[1]}")
print(f"second max salary={salary[-2]}")
