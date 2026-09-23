def biaya_hotel(jenis_kamar, durasi_menginap):

    if jenis_kamar ==  "Standard":
        biaya = 200000
    elif jenis_kamar == "Deluxe":
        biaya = 350000
    else:
        print("KAMAR TIDAK DITEMUKAN.")
        biaya = 0

    total_biaya = biaya * durasi_menginap
    return total_biaya

jenis_kamar = input("Masukkan Jenis Kamar (Standard/Deluxe): ")
check_in = int(input("Masukkan tanggal check-in : "))
check_out = int(input("Masukkan tanggal check-out : "))

durasi_menginap = check_out - check_in

total_biaya = biaya_hotel(jenis_kamar, durasi_menginap)

print("______________________")
print("\n   DETAIL PEMESANAN")
print("______________________")
print("Jenis Kamar     : ", jenis_kamar)
print("Check-in        : ", check_in)
print("Check-out       : ", check_out) 
print("Durasi Menginap : ", durasi_menginap, "malam")
print("Total Biaya     : Rp.", total_biaya)