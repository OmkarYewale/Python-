
products = {
    'P101': {"name": "Laptop", "price": 55000, "stock": 8},
    'P102': {"name": "Mouse", "price": 700, "stock": 25},
    'P103': {"name": "Keyboard", "price": 1200, "stock": 15},
    'P104': {"name": "Monitor", "price": 14000, "stock": 5},
    'P105': {"name": "Headphones", "price": 2500, "stock": 0},
    106: {"name": "Headphones", "price": 2500, "stock": 0}
}

employees = {
    101: {"name": "Amit", "department": "IT", "salary": 45000},
    102: {"name": "Priya", "department": "HR", "salary": 38000},
    103: {"name": "Sneha", "department": "IT", "salary": 52000},
    104: {"name": "Raj", "department": "Sales", "salary": 41000},
    105: {"name": "Anjali", "department": "HR", "salary": 47000},
    106: {"name": "pooja", "department": "HR", "salary": 47000},

}

# 41. Merge two dictionaries without using the | operator.
# merger_dict = products | employees
# for key , val in merger_dict.items():
#     print(key,val)
# # print(merger_dict)

# for key,val in employees.items():
#     products[key]=val

# for key,val in products.items():
#     print(key,val)

# 42. Find common keys between two dictionaries.
# keys=[]
# for key in products.keys():
#     if key in employees.keys():
#         keys.append(key)
# print(keys)

# 43. Find keys present in the first dictionary but not in the second.
# keys=[]
# for key in products.keys():
#     if key in employees.keys():
#         keys.append(key)
# print(keys)

# 44. Create a dictionary from two separate lists: one containing keys and another containing values.

keys= [101,102]
vlaues=[
    {'name':"omkar",'age':22},
    {'name':"pooja",'age':21}
    ]
new_dict ={}
count=0
for key in keys:
    new_dict[key]=vlaues[count]
    count+=1

# print(new_dict)

# 45. Reverse a dictionary so that values become keys and keys become values.
rev_dict={}
for key,val in new_dict.items():
    val[val['age']]='age'
print(rev_dict)

# 46. Count the frequency of every character in a user-given string using a dictionary.
# 47. Count the frequency of every word in a sentence.
# 48. Group student names by their city using a dictionary.
# 49. Sort a dictionary by its values in ascending order.
# 50. Remove duplicate values from a dictionary while keeping the first matching key