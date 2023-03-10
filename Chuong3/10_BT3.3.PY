x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))
sai="Khong hop le"
if (ch=='+' or ch =='-' or ch=='*' or ch=='/'):
    if (ch=='+'):
         print(x+y)
    if (ch=='-'):
         print(x-y)
    if (ch=='*'):
         print(round(x*y),1)
    if (ch=='/'):
        if (y!=0):
         print(round(x/y),1)
        else: 
         print(sai)
else:    print(sai)



