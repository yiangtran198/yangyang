def LaSoNguyenTo(x):
    d=0
    for i in range(1,x+1):
        if x%i==0:
            d=d+1
    if d==2:
        return True
    else:
        return False
def SoHopLe(x):
    if x<=1:
        return True
    else:
        return False
def NhapvaDem():
    x=int(input())
    s=0
    while SoHopLe(x)==True:
        x=int(input())
        if LaSoNguyenTo(x)==True:
            s=s+1  
    return s
def InKQ(kq):
    kq=NhapvaDem()
    print("Co",kq,"so nguyen to")
print("Nhap day so") 
a=NhapvaDem()
v=InKQ(a)
    
