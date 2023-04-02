import math 
def nhap():
    x=float(input())
    return x
def pytago(x,y):
     z=round(math.sqrt(x*x+y*y),1)
     return z
a=nhap()
b=nhap()
print("Do dai canh huyen:",pytago(a,b))

    
    