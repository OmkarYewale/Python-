#find min ,max,and average salary of employee homework

salary=[67000,45000,78000,55000,28000]
max_sal=salary[0]
min_sal=salary[0]
total_sal=0
for sal in salary:
    total_sal=total_sal+sal
    if sal>max_sal:
        max_sal=sal
    if sal<min_sal:
        min_sal=sal
average=total_sal/len(salary)
print(f"max salary of employee is = {max_sal}")
print(f"min salary of employee is = {min_sal}")
print(f"Average salary of employee is ={average}")