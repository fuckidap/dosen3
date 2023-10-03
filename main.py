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



# print('----------------')
# print('kasir')
# print('----------------')
#
# print(' ')
#
# HargaSusuPerBotol = 25000
# HargaBerasPerKg = 12000
# HargaTelurPerButir = 2000
# HargaSardenPerKg = 5000
#
# JumlahBotolSusu = int(input('Jumlah botol susu yang dibeli :'))
# JumlahKgBeras = int(input('Jumlah kilogram beras yang dibeli :'))
# JumlahTelur = int(input('Jumlah telur yang dibeli :'))
# JumlahKalengSarden = int(input('jumlah kaleng sarden yang dibeli :'))
#
# TotalHargaSusu = HargaSusuPerBotol * JumlahBotolSusu
# TotalHargaBeras = HargaBerasPerKg * JumlahKgBeras
# TotalHargaTelur = HargaTelurPerButir * JumlahTelur
# TotalHargaSarden = HargaSardenPerKg * JumlahKalengSarden
#
# TotalBelanjaan = TotalHargaSusu + TotalHargaBeras + TotalHargaTelur + TotalHargaSarden
#
# print('Total harga belanjaan adalah Rp.', TotalBelanjaan)





# print('--------------------------------')
# print('Menghitung Nilai Akhir Mahasiswa')
# print('--------------------------------')
#
# Nama = str(input('Masukan Nama Anda     :'))
# Uts = int(input('Masukan Nilai UTS     :'))
# Uas = int(input('Masukan Nilai UAS     :'))
# Tgs = int(input('Masukan Nilai Tugas   :'))
# Pyk = int(input('Masukan Nilai Proyek  :'))
#
# print('')
#
# print('Mahasiswa yang bernama ' + Nama)
# print('Dengan Nilai Presentasi yang dihasilkan')
#
# nilaiuts = Uts*(30/100)
# nilaiuas = Uas*(40/100)
# nilaitugas = Tgs*(15/100)
# nilaiproyek = Pyk*(15/100)
# nilaiakhir = nilaiuts+nilaiuas+nilaitugas+nilaiproyek
#
# print('Nilai UTS * 30%    : ', nilaiuts)
# print('Nilai UAs * 40%    : ', nilaiuas)
# print('Nilai Tugas * 15%  : ', nilaitugas)
# print('Nilai Proyek * 15% : ', nilaiproyek)
#
# print('')
#
# print('Nilai Akhir yang diperoleh Mahasiswa dengan Nama ' + Nama + ' (NIM: ' + Nim + ')' ':', nilaiakhir)




# print('--------------------------------')
# print('Menghitung Nilai Akhir Mahasiswa')
# print('--------------------------------')
#
# Nama = str(input('Masukan Nama Anda     :'))
# Nim = str(input('Masukan Nim Anda      :'))
# BobotUts = int(input('Masukan bobot UTS (dalam persentase) :'))
# BobotUas = int(input('Masukan bobot UAS (dalam persentase) :'))
# BobotTugas = int(input('Masukan bobot Tugas (dalam persentase) :'))
# BobotProyek = int(input('Masukan bobot Proyek (dalam persentase) :'))
# Uts = int(input('Masukan Nilai UTS     :'))
# Uas = int(input('Masukan Nilai UAS     :'))
# Tgs = int(input('Masukan Nilai Tugas   :'))
# Pyk = int(input('Masukan Nilai Proyek  :'))
#
# print('')
#
# print('Mahasiswa yang bernama ' + Nama + '(NIM: ', Nim + ')')
# print('Dengan Nilai Presentasi yang dihasilkan')
#
# nilaiuts = Uts*(BobotUts/100)
# nilaiuas = Uas*(BobotUas/100)
# nilaitugas = Tgs*(BobotTugas/100)
# nilaiproyek = Pyk*(BobotProyek/100)
# nilaiakhir = nilaiuts+nilaiuas+nilaitugas+nilaiproyek
#
# print('Nilai UTS * 30%    : ', nilaiuts)
# print('Nilai UAs * 40%    : ', nilaiuas)
# print('Nilai Tugas * 15%  : ', nilaitugas)
# print('Nilai Proyek * 15% : ', nilaiproyek)
#
# print('')
#
# print('Nilai Akhir yang diperoleh Mahasiswa dengan Nama ' + Nama + ' (NIM: ' + Nim + ')' ':', nilaiakhir)


print('----------------------------------------------')
print('Simulasi Menabung Rutin dengan bunga Berbunga')
print('----------------------------------------------')


JumlahYangDiTabung = int(input('Masukan jumlah awal yang akan ditabung (dalam Rupiah) :'))
BungaTahunan = int(input('Masukan tingkat bunga tahunan (dalam persentase) :'))
PeriodeTabungan = int(input('Masukan periode tabungan (dalam tahun) :'))
TabunganRutinPerTahun = int(input('Masukan jumlah tabungan rutin per tahun (dalam Rupiah) :'))


JumlahAkhir = JumlahYangDiTabung * (1 + BungaTahunan/100)**PeriodeTabungan + TabunganRutinPerTahun * PeriodeTabungan

print('Setelah', PeriodeTabungan, 'jumlah uang yang akan Anda miliki adalah RP.', JumlahAkhir)

