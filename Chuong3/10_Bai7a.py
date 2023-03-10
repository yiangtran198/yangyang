n=int(input(""))
if n==0:
    s=1
    print(s)
else:
    while n>0:
        s=1
        i=1
        while i<=n:
            s=s*i
            i=i+1
        print(s)
        n=int(input(""))