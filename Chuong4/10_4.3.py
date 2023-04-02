
import math
def nhap():
    x=int(input())
    return x
def giaipt(a,b,c):
    delta=b*b-4*a*c
    if delta <0:
        print("Phuong trinh vo nghiem")
    elif delta==0:
        print("Phuong trinh co nghiem kep")
    else:
        print("Phuong trinh co 2 nghiem phan biet")
def inkq(x1,x2):
    a=int
    b=int
    c=int
    x1=(-b+ math.sqrt(b))/2*a
    x2=(-b- math.sqrt(b))/2*a
a=print("a=",nhap())
b=print("b=",nhap())
c=print("c=",nhap())
v=giaipt(a,b,c)
inkq()