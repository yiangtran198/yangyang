ch=str(input())
n=int(input())
if n>=1 and n<=20:
    i=1 
    while i<=n:
        j=1
        while j<=i:
            print(ch,end=" ")
            j=j+1
        print()
        i=i+1