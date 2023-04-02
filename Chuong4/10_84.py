def nhap():
    x=int(input())
    return x
def tb(x,y,z):
  if z==y+1==x+2 :
    return (y)
  if x==y+1==z-1:
    return x
  if x==y+1==z+2:
    return y
  else:
    return ((x+y+z)/3)
a=nhap()
b=nhap()
c=nhap()
print("trung vi cua ba so:",tb(a,b,c))
