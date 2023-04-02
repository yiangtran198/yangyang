def nhap():
    x=int(input("Nhap sp luong muc cho don hang:"))
    return x
def tien_van_chuyen(so_muc):
    muc_dau=10.95 
    if so_muc==1:
        return 10.95
    elif so_muc>1:
        return 10.95+0.25*(so_muc -1)
n=nhap()
print("Tong tien van chuyen là:",tien_van_chuyen(n))
    
