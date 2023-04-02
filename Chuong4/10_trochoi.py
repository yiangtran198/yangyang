import random 
n=int(input("Nguoi:"))
r=random.randint(1,3)
        # n=int(input("n="))
        # r=random.randint(1,3)
        # print("May:",r)
        # kq=kq(n,r)
def kq(x,r):
    while x>0 and x<4:
        if x==r:
            print("Hoa nhau")
            break
        elif x==1 and r==2:
            print("Nguoi thang")
            break
        elif x==2 and r==3:
            print("Nguoi thang")
            break
        elif x==3 and r==1:
            print("Nguoi thang")
            break
        elif r==1 and x==2:
            print("May thang")
            break
        elif r==2 and x==3:
            print(" May thang")
            break
        elif r==3 and x==1:
            print("May thang")
            break
kt=kq(n,r)
while n!=0:
        n=int(input("n="))
        r=random.randint(1,3)
        kq=kq(n,r)
# a=int(input('Nguoi: '))
# import random
# r=random.randint(1,3)
# print('May: ',r)
# while True:
#     if a==1 and r==2:
#         print('Nguoi thang')
#         break
#     elif a==2 and r==3:
#         print('May thang')
#         break
#     elif a==r:
#         print('Hoa')
#         break
#     elif a==1 and r==3:
#         print('May thang')   
#         break
#     elif a==2 and r==1:
#         print('May thang')
#         break
#     elif a==3 and r==1:
#         print('Nguoi thang')
#         break
#     elif a==3 and r==2:
#         print('May thang')
#         break
#     if a==0:
#         break
            