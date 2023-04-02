def nhap():    #nhap 3 số
    x=int(input())
    return x
def max3(a,b,c):  #tìm giá trị max
    max=a
    if max<b :
        max=b
    if max<c:
        max=c
    return max
def inkq(kq):
    print("So lon nhat la:",kq)
print("Nhap 3 so nguyen")
a=nhap()
b=nhap()
c=nhap()  
v=max3(a,b,c)
inkq(v)    