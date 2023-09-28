# print("=======================")
# print("Buku Tamu Undangan")
# print("=======================")
# print(" ")
# print("=======================")
# Nim_Anda = str(input("Input Nim : "))
# Nama_Anda = str(input("Input Nama : "))
# print("Selamat datang " + Nim_Anda +" "+ Nama_Anda + "di perpustakaan Buddhi Dharma")

# print("================")
# print("Konversi Suhu Celsius ke Fahrenheit")
# print("================")
# print(" ")
# Celcius = int(input("Input Suhu Dalam Celcius: "))
#
# Fahrenheit = (9/5 * Celcius) + 32
# print("Hasil Konverensi :")
# print(Celcius, "Celcius" + " " + "=", Fahrenheit, "Fahrenheit")




# print("=============================")
# print("Perhitungan Keuntungan Saham ")
# print("=============================")
# HargaAwalPerSaham = int(input("input harga awal saham (Rp): "))
# HargaAkhirPerSaham = int(input("input harga  akhir saham (Rp): "))
# JumlahSaham = int(input("input jumlah saham : "))
#
# TotalAwalSaham = HargaAwalPerSaham * JumlahSaham
# TotalAKhirSaham = HargaAkhirPerSaham * JumlahSaham
# TotalKeuntungan = TotalAKhirSaham - TotalAwalSaham
# Presentase_Keuntungan = TotalKeuntungan / HargaAwalPerSaham * 100
#
#
# print(" ")
# print("---------------------------------")
# print("Keuntungan Setelah Awal Tahun : ")
# print("---------------------------------")
#
# print("Harga Awal Per Saham  : RP.", HargaAwalPerSaham, ".00")
# print("Harga Akhir Per Saham : RP.", HargaAkhirPerSaham, ".00")
# print("Jumlah Saham          :", JumlahSaham)
# print("Total keuntungan      :", TotalKeuntungan, ".00")
# print("Presentase Keuntungan :", Presentase_Keuntungan, "%")





# print("----------------")
# print("Menghitung Bunga Pinjaman Online")
# print("----------------")
#
# JumlahPinjaman = int(input("Jumlah pinjaman (RP) : "))
# TingkatBungaTahunan = int(input("Tingkat Bunga Tahunan (%) : "))
# JangkaWaktuPinjaman = int(input("Jangka Waktu Pinjaman (bulan) : "))
#
# print(" ")
# print("-------------------")
# print("Hasil Perhitungan ")
# print("------------------")
#
# print("Jumlah pinjaman (Rp):", JumlahPinjaman)
# print("Tingkat Bunga Tahunan (%):", TingkatBungaTahunan)
# print("Jangka waktu Pinjaman (bulan) :", JangkaWaktuPinjaman)
#
# print("")
#
# TotalJumlah = JumlahPinjaman+(JumlahPinjaman * TingkatBungaTahunan/100 * JangkaWaktuPinjaman/12)
#
# print("Total Jumlah yang harus dibayarkan oleh Andi setelah", JangkaWaktuPinjaman)
# print("Bulan : Rp.", TotalJumlah)
# print("Terima kasih telah menggunakan program ini!!")





# NamaPengguna = (input("Masukan Nama Pengguna :"))
# print("Halo " + NamaPengguna + "! Selamat datang ke Program Python sederhana")

print('----------------')
print('kasir')
print('----------------')

print(' ')

HargaSusuPerBotol = 25000
HargaBerasPerKg = 12000
HargaTelurPerButir = 2000
HargaSardenPerKg = 5000

JumlahBotolSusu = int(input('Jumlah botol susu yang dibeli :'))
JumlahKgBeras = int(input('Jumlah kilogram beras yang dibeli :'))
JumlahTelur = int(input('Jumlah telur yang dibeli :'))
JumlahKalengSarden = int(input('jumlah kaleng sarden yang dibeli :'))

TotalHargaSusu = HargaSusuPerBotol * JumlahBotolSusu
TotalHargaBeras = HargaBerasPerKg * JumlahKgBeras
TotalHargaTelur = HargaTelurPerButir * JumlahTelur
TotalHargaSarden = HargaSardenPerKg * JumlahKalengSarden

TotalBelanjaan = TotalHargaSusu + TotalHargaBeras + TotalHargaTelur + TotalHargaSarden

print('Total harga belanjaan adalah Rp.', TotalBelanjaan)

