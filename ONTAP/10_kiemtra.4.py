n=str(input())
tong=0
if len(n)==1:
 	print(0)
else:
  tong=((int(n)%100)//10+int(n)%100)%10
print(tong) 