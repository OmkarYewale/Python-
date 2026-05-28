#Genrate electricity bill on the basis of given condition
#Task 2 :-> smart electricity bill generator
#  input -> number of electricity units,
#  conditin:-> units =300 extra surcharge rs 500 otherwise surcharge rs 100
#total_bill=unit*8
#print total bill  units=8
#units 0 to 50 -->  no bill
#units 51 to 100 --> 5 rs /unit
#units above 101 -->8 rs /unit

unit=int(input("enter total unit  to genrate bill = "))
total_bill=0
if unit<50:
    print(f"you dont need to pay bill")
elif unit>50 and unit <100:
    total_bill =unit * 5
elif unit>=100 and unit<300:
    total_bill = unit * 8
    total_bill +=100
else:
    total_bill = unit * 8
    total_bill +=500
GST=total_bill*18/100
print(f"Total bill is = {total_bill+GST}")