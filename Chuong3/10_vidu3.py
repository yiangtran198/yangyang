yrsofserve=input("yrsofserve=")
salary=input("salary=")
bonus=input("bonus=")
if yrsofserve < 5:
     if salary <500:
        bonus = 100 
     else:
       bonus = 200
else:
    bonus = 700
print("bonus amount: ", bonus)
