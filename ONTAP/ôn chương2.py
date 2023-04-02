# #2.1ontap
# A=input("Nhap ho ten:")
# print("Chao ban",A,"!!!")
#2.2ontap
# a=int(input("Nhap Gia niem yet: "))
# b=int(input("Nhap gia chiet khau: "))
# c=(a-b)*0.01
# print("Gia ban: ",(a-b)+c)
#2.3ontap
# a=int(input("Tien dau tu ban dau: "))
# b=int(input("So thang gui: "))
# c=float(input("Lai suat moi thang: "))
# print("Tien lanh cuoi ky: ",round(a*(1+b*c),1))
#2.4ontap
# import math 
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# s=(a+b+c)/2
# d=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("Dien tich=",end="")
# print(d)
             #2.2
# r=int(input("NHap vao ban kinh cua duong tron: "))
# print("Dien tich cua duong tron có ban kinh",r,"la =",round(3.14*r*r,1))
# print("Chu vi cua duong tron co ban kinh",r,"la =",round(2*r*3.14,1))
            #2.3
            #2.4
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# d=float(input("d="))
# print('Tong=',end="")
# print(round(a+b+c+d,1))
# print("Trung binh cong=",end="")
# print(round((a+b+c+d)/4,1))
        #2.5
# N=float(input("So tien ban dau:"))
# k=int(input("So thang gui:"))
# r=float(input("Lai suat/thang:"))
# print("Voi so tien ban dau",round(N),end="")
# print(", sau",k,"thang gui",end="")
# print(", lai suat",r,end="")
# print("/ thang")
# m=N*(1+k*r)
# print("Thi so tien nhan suoc cui ky la:",m)
    #2.6
a=input("Ho ten:")
b=int(input("So ngay cong:"))
c=float(input("Don gia ngay cong:"))
d=float(input("He so phu cap:"))
e=float(input("Tam ung:"))
l=c*b*d
t=l-e
print("Nhan vien",a,end="")
print(", Co tien luong=",end="")
print(round(l,1),end="")
print(", Tam ung=",end="")
print(round(e),"va Thuc linh=",end="")
print(round(t,1))