products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 8},
    "P102": {"name": "Mouse", "price": 700, "stock": 25},
    "P103": {"name": "Keyboard", "price": 1200, "stock": 15},
    "P104": {"name": "Monitor", "price": 14000, "stock": 5},
    "P105": {"name": "Headphones", "price": 2500, "stock": 0}
}


# 31. Print the name and price of every product

# for key,value in products.items():
#     print(f"name : {value["name"]} and price : {value['price']}")

#  Print products having stock less than 10.

# for value in products.values():
#     if value['stock']<10:
#         print(value)

#  Print products that are out of stock

# for value in products.values():
#     if value['stock'] == 0:
#         print(value)

# total_price = {}

# for key,value in products.items():
#     total = value['price'] * value['stock']
#     total_price[f'{key} total_price']= total
# print(total_price)

# 35. Find the most expensive product.
# 36. Find the cheapest product.

# max = 0
# for key,value in products.items():
#     if value['price']>max:
#         max=value['price']

# for key ,value in products.items():
#     if max in value.values():
#         print(key,value," is expensive product")

# cheapest =products["P101"]['price']
# for key,value in products.items():
#     if value['price']<cheapest:
#         cheapest=value["price"]

# for key, value in products.items():
#     if value["price"]==cheapest:
#         print(key,value," is cheapest product")

# 37. Create a list containing the names of all available products.

# pro_name_list = []

# for val in products.values():
#     pro_name_list.append(val['name'])
# print(pro_name_list)

# 38. Create a dictionary containing product name as key and stock as value

# new_pro_dict = {}
# for val in products.values():
#     new_pro_dict[val['name']]=val['stock']
# print(new_pro_dict)

# 39. Update the stock of product P104 to 12.

# if 'P104' in products.keys():
#     products["P104"]['stock']=12
# print(products)

# 40. Apply a 5% discount to all products costing more than 10,000

for key,value in products.items():
    if value['price']>10000:
        discount = value["price"] * 5/100
        value["price"]=value['price']-discount

for key,val in products.items():
    print(key,val)