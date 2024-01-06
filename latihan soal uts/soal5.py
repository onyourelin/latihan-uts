def hitung_kpk(b1,b2):
    calon_kpk = b1
    kpk_ketemu = False
   
    while not kpk_ketemu:
        if calon_kpk % b2 == 0:
            kpk_ketemu = True
        else:
            calon_kpk = calon_kpk + b1
           
            return calon_kpk
        
b1 = int(input("b1: "))
b2 = int(input("b2: "))
       
hasil_kpk = hitung_kpk(b1,b2)
print(f"KPK dari {b1} dan {b2} adalah {hasil_kpk}")