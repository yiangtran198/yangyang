# n=int(input("n="))
# if n>0:
#     if n%2==0:
#         print("the munber is even")
#     else:
#         print("The number is odd")
# else:
#     print("The number is negative")
#3.1ontap
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# max=a
# if max<b:
#     max=b 
# if max<c:
#     max=c
# print("SLN",max)
# min=a
# if min>b:
#    min=b
# if min>c:
#     min=c
# print("SNN",min)
# n=int(input("So may="))
# if n>5:
#     s=n*450
# else: 
#     s=n*500
# print("So tien=",s)
# n=int(input("Tieu thu="))
# s=0
# if n<100:
#     s=n*550
# elif n<=150:
#     s=100*550+(n-100)*750
# elif n<=200:
#     s=100*550+50*750+(n-150)*950
# elif n>200:
#     s=100*550+50*750+50*950+(n-200)*1350
# d=s+0.1*s
# print("Phai tra=",round(d,1))
    #3.1
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# import math
# p=0
# s=0
# if (a+b)>c and (a+c)>b and (b+c)>a:
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("Dien tich=",end="")
#     print(round(s,3))
# else:
#     print("Khong hop le")
    #3.2
# m1=int(input("M1="))
# m2=int(input("M2="))
# m3=int(input("M3="))
# s=int(input("S="))
# d=0
# if s<100:
#     d=s*m1
# if s<=150:
#     d=100*m1+(s-100)*m2
# if s>150:
#     d=100*m1+50*m2+(s-150)*m3
# print("Phai tra=",end="")
# print(round(d))
# x=float(input("x="))
# y=float(input("y="))
# ch=str(input("Phep toan:"))
# sai="Khong hop le"
# if ch=="+" or ch=="-" or ch=="/" or ch=="*":
#     if ch=="+":
#         print(str(x) + "+" +str(y) + "=" + str(round(x+y,1),))
#     if ch=="-":
#         print(str(x) + "-" + str(y) + "=" + str(round(x-y,1)))
#     if ch=="*":
#         print(x,"*",y,"=",round(x*y,1),sep="")
#     if ch =="/":
#         if y>0:
#             print(x,"/",y,"=",round(x/y,1),1,sep="")
#         else: print(sai)
# else:
#     print(sai)
    #3.4
# t=float(input())
# l=float(input())
# h=float(input())
# dtb=(t*2+l*3+h)/6
# if dtb<3:
#     print("Kem")
# elif dtb>=3 and dtb <5 :
#     print("Yeu")
# elif dtb>=5 and dtb <6 :
#     print("Trung binh")
# elif dtb>=6 and dtb <7:
#     print("Trung binh kha")
# elif dtb>=7 and dtb <8:
#     print("Kha")
# elif dtb>=8 and dtb <9:
#     print("Gioi")
# elif dtb>=9 and dtb <10:
#     print("Xuat sac")
#3.5
# n=int(input(""))
# if n==0:
#     print("Xep loai A")
# elif n<2:
#     print("Xep loai B")
# elif n<4:
#     print("Xep loai C")
# else :print("Xep loai D")
#3.6
# a=float(input())
# b=float(input())
# c=float(input())
# if ((a + b> c) and (a + c > b) and (b + c > a) and (a> 0) and (b > 0) and (c > 0)):
#     if (a*a==b*b+c*c) or (b*b ==a*a+c*c) or (c * c == a * a + b* b):
#             print("Tam giac vuong")
#     elif ((a==b) and (b==c) and(c==a)):
#             print("Tam giac deu")
#     else : print("Tam giac loai khac")
# else:  print("KHong hop le")
    #4ontap
a=float(input("a="))
b=float(input("b="))
ch=str(input("Toan tu:"))
sai="Khong hop le"
while True:
    d=input("Tiep tuc")
    a=float(input("a="))
    b=float(input("b="))
    ch=str(input("Toan tu:"))
    if ch=="+" or ch=="-" or ch=="/" or ch=="*":
        if ch=="+":
            print(str(a) + "+"+ str(b)+"="+str(round(a+b,1)))
        if ch=="-":
            print(a+"-"+ b+"="+round(a-b,1))
        if ch=="*":
            print(a+"*"+b+"="+round(a*b,1))
        if ch =="/":
            if b>0:
                print(a,"/",b,"=",round(a/b,1),1,sep="")
            else: print(sai)
    if d=="t" or d=="T":
        break
       #3.7
# n=int(input())
# if n==0:
#     s=1
#     print(s)
# else:
#     while n>0:
#         s=1
#         i=1    
#         while i<=n:
#             s=s*i
#             i=i+1
#         print(s) 
#         n=int(input()) 
#3.11
# 
     
     
            