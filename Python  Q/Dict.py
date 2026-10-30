employees = {
    101: {"name": "Amit", "department": "IT", "salary": 45000},
    102: {"name": "Priya", "department": "HR", "salary": 38000},
    103: {"name": "Sneha", "department": "IT", "salary": 52000},
    104: {"name": "Raj", "department": "Sales", "salary": 41000},
    105: {"name": "Anjali", "department": "HR", "salary": 47000},
    106: {"name": "Pooja", "department": "HR", "salary": 1000000}
}

# for key,value in employees.items():
#     print(employees[key]['name'])

# for key,valule in employees.items():
#     print(f"key :{key} and name : {employees[key]['name']}")

# for key , value in employees.items():
#     if "IT" in employees[key]['department']:
#         print(f"{key,value}")

# for key,value in employees.items():
#     if value['salary']>40000:
#         print(f"{key,value}")

# max=0
# for key ,value in employees.items():
#     if value['salary']>max:
#         max=value["salary"]

# for key in employees:
#     if employees[key]['salary']==max:
#         print(f"{employees[key]['name']} has the highest salary.")
# low=employees[101]['salary']
# for key , value in employees.items():
#     if value['salary']<low:
#         low=value['salary']

# for key in employees:
#     if employees[key]['salary']==low:
#         print(f"{employees[key]['name']} has lowest salary.")

# total_sum = 0
# for key in employees:
#     total_sum = employees[key]['salary'] + total_sum

# print(f"total salary of all employess is {total_sum}")
# print(f"avg of salary of employees is {total_sum/len(employees)}")

# each_dep_dict = {}
# for key , value in employees.items():
#     count = 0
#     for key1,value2 in employees.items():
#         if value2['department'] ==value['department']:
#             count += 1
#     each_dep_dict[value["department"]]=count

# print(each_dep_dict)

# for key,value in employees.items():
#     inc_sal=value['salary']*0.10
#     value["salary"]=value["salary"] + inc_sal
# print(employees)

# 26.Create a new dictionary containing employee names and salaries.
# 27. Create a new dictionary containing only HR employees.
# names_salary ={}
# HR = {}
# for key ,value in employees.items():
#     names_salary ['name']=value['name']
#     names_salary['salary']=value['salary']
#     if value['department'] == 'HR':
#         HR[key] = value

# print(names_salary)
# print(HR)

# . Find whether employee ID 103 exists

# for key in employees:
#     if key==103:
#         print("employes id 103 exist in dict")

if 105 in employees:
    print("employes id 103 exist in dict")


#  Remove employee ID 104 from the dictionary

# del employees[103]
# employees.pop(105)
# print(employees)