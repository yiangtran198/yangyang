def nhap():
    # if x>=2:
    x=int(input("n="))
    return x
def inkq(n):
        for i  in range (1,n+1):
            if i%2==0:
                print(i,end=" ")
while True:
        n=nhap()
        v=inkq(n)
        d=str(input("Tiep tuc khong?"))
        if d=="k" or d=="K":
            break    
        
        
    
    
     