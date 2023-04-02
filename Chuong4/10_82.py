def nhap():
    x=float(input("Quang duong da di(km):"))
    return x
def gia_ve(quang_duong):
    quang_duong_met=quang_duong *1000  #đổi sang mét  
    giacb=4
    tong_gv=giacb+(quang_duong_met/140)*0.25
    return tong_gv
n=nhap()
print("Tong gia ve là:",gia_ve(n))
