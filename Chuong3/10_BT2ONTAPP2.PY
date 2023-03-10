n=int(input("n="))
while n<=0:
        print("Khong hơp le!!!\nMoi nhap lai")
        n=int(input("n="))
i=1
s=0
while i<=n:
    if n % i==0:
        s=s+1
        i=i+1
if s==2:
        print(n,"la SNT")
else:
        print(n,"khong la SNT")