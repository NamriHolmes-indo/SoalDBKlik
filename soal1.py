def check_order(ambil, makan_di_tempat, dilayani):
    i = 0 
    j = 0 
    
    for order in dilayani:
        if i < len(ambil) and order == ambil[i]:
            i += 1
        elif j < len(makan_di_tempat) and order == makan_di_tempat[j]:
            j += 1
        else:
            return False
    
    return i == len(ambil) and j == len(makan_di_tempat)

ambil = [1, 3, 5]
makan_di_tempat = [2, 4, 6]
dilayani = [1, 2, 4, 6, 5, 3]

if check_order(ambil, makan_di_tempat, dilayani):
    print("Kondisi 1: Pesanan diproses sesuai dengan prinsip siapa cepat dia dapat.")
else:
    print("Kondisi 1: Ada ketidaksesuaian dalam proses pemesanan.")

ambil = [17, 8, 24]
makan_di_tempat = [12, 19, 2]
dilayani = [17, 8, 12, 19, 24, 2]

if check_order(ambil, makan_di_tempat, dilayani):
    print("Kondisi 2: Pesanan diproses sesuai dengan prinsip siapa cepat dia dapat.")
else:
    print("Kondisi 2: Ada ketidaksesuaian dalam proses pemesanan.")
