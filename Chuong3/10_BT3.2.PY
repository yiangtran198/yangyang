m1=float(input('M1='))
m2=float(input('M2='))
m3=float(input('M3='))
s=int(input("S="))
if s<=100:
    p=m1*s
elif s<=150:
    p=m1*100+m2*(s-100)
else:
    s>=151 
    p=100*m1+m2*50+m3*(s-150)
print("Phai tra=",round(p))
