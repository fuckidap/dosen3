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






# print('----------------------------------------------')
# print('Simulasi Menabung Rutin dengan bunga Berbunga')
# print('----------------------------------------------')
#
#
# JumlahYangDiTabung = int(input('Masukan jumlah awal yang akan ditabung (dalam Rupiah) :'))
# BungaTahunan = int(input('Masukan tingkat bunga tahunan (dalam persentase) :'))
# PeriodeTabungan = int(input('Masukan periode tabungan (dalam tahun) :'))
# TabunganRutinPerTahun = int(input('Masukan jumlah tabungan rutin per tahun (dalam Rupiah) :'))
#
#
# JumlahAkhir = JumlahYangDiTabung * (1 + BungaTahunan/100)**PeriodeTabungan + TabunganRutinPerTahun * PeriodeTabungan
#
# print('Setelah', PeriodeTabungan, 'jumlah uang yang akan Anda miliki adalah RP.', JumlahAkhir)





# a = int(input('Masukan nilai a :'))
# b = int(input('Masukan nilai b :'))
# c = int(input('Masukan nilai c :'))
#
# ekspresi1 = a + 4 < 10
# ekspresi2 = b > a + 5
# ekspresi3 = c - 3 >= 4
#
# ekspresi4 = ekspresi1 and ekspresi2 and ekspresi3
#
# print('/n')
# print('Program Ekspresi AND')
# print(f'Hasil dari ekspresi1 = a + 4 < 10 adalah {ekspresi1}')
# print(f'Hasil dari ekspresi2 = b > a + 5 adalah {ekspresi2}')
# print(f'Hasil dari ekspresi3 = c - 3 >= 4 adalah {ekspresi3}')
# print(f'Hasil dari ekspresi4 = ekspresi1 and ekspresi2 and ekspresi3 adalah {ekspresi4}')



# print('------------------------------------------')
# print('Kalkulator Pemasukan dan Pengeluaran Budi')
# print('------------------------------------------')
#
#
# gajiperjam = int(input('Masukan gaji per jam yang Anda inginkan :'))
# jumlahjamkerja = int(input('Masukan jumlah jam kerja dalam 1 minggu :'))
#
# sebelumbayarpajak = gajiperjam * jumlahjamkerja
# setelahbayarpajak = sebelumbayarpajak - 14/100
# belipakaiandanaksesoris = gajiperjam * jumlahjamkerja - 10/100
# belialattulis = gajiperjam * jumlahjamkerja - 1/100
#
#
#
#
# print('Pendapatan Budi selama libur musim panas sebelum pajak : Rp.', sebelumbayarpajak)
# print('Pendapatan Budi selama libur musim panas setelah pajak : Rp.', setelahbayarpajak)
# print('Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris : Rp', belipakaiandanaksesoris)






# print('------------------------')
# print('Program Hitung Rata-Rata')
# print('------------------------')

# nama = input('Masukan Nama Siswa :')
# nilai1 = float(input('Masukan Nilai Pertandingan I :'))
# nilai2 = float(input('Masukan nilai Pertandingan II :'))
# nilai3 = float(input('Masukan Nilai Pertandingan III :'))

# ratarata = (nilai1 + nilai2 + nilai3) / 3

# print('------------------------')
# print('    Hasil Perhitungan  ')
# print('------------------------')

# if nilai1 >= 85:
#     hadiah = ('komputer') 
# elif nilai2 >= 70:
#     hadiah = ('Uang')
# elif nilai3 <= 70:
#     hadiah = ('Hiburan')

# print('Nama Siswa :'+ nama)
# print('Nilai Rata-Rata :', ratarata) 
# print('')
# print('Selamat, Anda Mendapatkan Hadiah:'+hadiah)


print('------------------------')
print('Program Harga Paket Data')
print('------------------------')

print('Pilihan Operator (kode):')
print('- T: Telkomsel')
print('- I: Indosat')
print('- X: XL Axiata')

op = input('Masukan kode Operator:')

print('Pilihan Besaran Paket (kode):')
print('- A: 2GB')
print('- B: 5GB')
print('- C: 10GB')


paket = input('Masukan kode Besaran Paket: ')
jumlah = int(input('Masukan Jumlah Pembelian (dalam jumlah paket): '))
total = paket*jumlah

if op ('T') or paket ('A'):
    harga = ('30.000')

elif op ('T') or paket ('B'):
     harga = ('50.000')
elif op ('T') or paket ('C'):
     harga = ('90.000')

print('Informasi Paket yang Dibeli:')
print('Operator:' + op)
print('Besaran paket:', paket)
print('Jumlah Pembelian:',jumlah)
print('Total Harga:',total)







# pendapatan = float(input("Masukkan pendapatan harian: "))
# jasa = 0
# komisi = 0
# if pendapatan >= 0 and pendapatan <= 20000:
#     jasa = 10000
#     komisi = 0.1 * pendapatan
# elif pendapatan <= 50000:
#     jasa = 20000
#     komisi = 0.15 * pendapatan
# else:
#     jasa = 30000
#     komisi = 0.2 * pendapatan
# # Menghitung total pendapatan
# total = jasa + komisi
# print("Uang Jasa: Rp.", jasa)
# print("Uang Komisi: Rp.", komisi)
# print("===========================")
# print("Total Pendapatan: Rp.", total)

# match op.upper():
#     case 'T' 'A':
#         print('30.000')
#     case 'T' 'B':
#         print('50.000')
#     case 'T' 'C':
#         print('90.000')

