
count=1
while True:
    pin=int(input("Please Enter your  4 Digit Pin :"))
    DBPIn=7845
    if DBPIn==pin:
        print("Successful login ")
        break
    elif count==3:
        print("You attempts too many time . Try after some time .")
        break
    else:
        count+=1
        print("Please Enter currect Pin ")

