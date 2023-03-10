n=int(input())
l=list(str(n))
if n>=0 and n<=9999:
    for i in range(0,len(l)): 
        b=l[i]
        if b == '0' :
            print ('A',end = '') 
        elif b == '1' :
            print ('B',end = '') 
        elif b == '2' :
            print ('C',end = '') 
        elif b == '3' :
            print ('D',end = '') 
        elif b == '4' :
            print ('E',end = '') 
        elif b == '5' : 
            print ('F',end = '') 
        elif b == '6' :
            print ('G',end = '') 
        elif b == '7' :
            print ('H',end = '') 
        elif b == '8' :
            print ('K',end = '')