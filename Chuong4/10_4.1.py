def nhap():
    x=int(input("n="))
    return x
def giaithua(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
def inkq(n,X):
    print(n,'!=',X,sep="") 
n=nhap()
# d=giaithua(n) 
v=inkq(n,giaithua(n))
  