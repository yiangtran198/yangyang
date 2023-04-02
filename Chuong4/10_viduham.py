# def Nhap():
#      print("NHap mot so nguyen")
#      n=int(input("n="))
#      return n 
# def Tinh(n):
#     s=0
#     for x in range(1,n+1):
#         s=s+x
#     return s
# def inkq(n,s):
#     print("tong cua",n,"so nguyen duong dau tien=",s,sep="")
# n=Nhap()
# s=Tinh(n)
# inkq(n,s)

# def show_nuner(m,n):
#     for i in range (m,n+1):
#       print(i)
      
# show_nuner(1,4)  
# def show_number(m=1,n=10):
#     for i in range(m,n+1):
#         print(i)
# show_number(3,7)
# show_number(3,)
# def NHap():
#     x=int(input("x="))
#     y=int(input("y="))
#     return x,y
# a,b=NHap()
# print("Hai so nguyen da nhap=",a,b)
# def nhap():
#     n=int(input("n="))
#     return n 
# def nhapvadem(n):
#     print("Nhap",n,"so nguyen:")
#     d=0
#     for i in range(1,n+1):
#         n= int(input())
#         if i%2==0 and i!=0:
#             d=d+1
#     return d
# def inkq(x):
#     print("So chu so chan",x)
# n=nhap()
# t=nhapvadem(n)
# n=inkq(t)
def nhap():
    x=int(input("x="))
    global y
    y=5 
    return x+y
kq=nhap()
print("y=",y)
print("kq=",kq)
