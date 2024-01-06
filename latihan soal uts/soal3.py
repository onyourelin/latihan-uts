def bisa_memilih(usia,status_perkawinan):
    if usia >= 17 or status_perkawinan:
        return True
    else:
        return False
   
print(bisa_memilih(20, True))