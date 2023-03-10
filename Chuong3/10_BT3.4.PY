t=float(input(""))
l=float(input(""))
h=float(input(""))
tb=((t*2)+(l*3)+h)/6
if tb<3:
    print("Kem")
elif (tb>=3) and (tb<5):
    print("Yeu")
elif ((tb>=5)) and (tb<6):
    print("Trung Binh")
elif (tb>=6) and (tb<7):
    print("Trung Binh Kha")
elif (tb>=7) and (tb<8):
    print("Kha")
elif (tb>=8) and (tb<9):
    print("Gioi")
else: 
    print("Xuat sac")

