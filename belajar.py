# total_belanja = int(input("Berapa total belanjaan Anda? "))
# if (total_belanja) >= 100000:
#     discount = 0.1
#     print("Selamat! Anda mendapatkan diskon sebesar 10 persen")
# else:
#     discount = 0
#     print("Anda tidak mendapatkan diskon")

# total = total_belanja - (total_belanja * discount) 
# str(print("Jadi total belanja yang harus Anda bayar adalah ")), (print(total))

# nilai_ujian = int(input("Berapa nilai ujian Anda? "))
# if nilai_ujian >= 70:
#     print("Selamat! Anda lulus.")
# else:
#     print("Mohon maaf, kamu harus mengulang mata kuliah tersebut.")

# nilai_ujian = int(input("Berapa nilai ujian Anda? "))
# if nilai_ujian >= 85:
#     print("Nilai Anda A")
# elif nilai_ujian >= 70 and nilai_ujian < 85:
#     print("Nilai Anda B")
# elif nilai_ujian >= 60 and nilai_ujian < 70:
#     print("Nilai Anda C")
# else:
#     print("Mohon maaf Anda belum lulus.")

# print("=" * 55)

# nilai_ujian = int(input("Berapa nilai ujian Anda? "))
# if nilai_ujian >= 85:
#     print("Grade A")
# elif nilai_ujian >= 70:
#     print("Grade B")
# elif nilai_ujian >= 60:
#     print("Grade C")
# else:
#     print("Tidak lulus")

# print("=" * 55)

# for i in [3, 5, 1, 4, 2]:
#     print("urutan ke", i)

# urutan = [3, 5, 1, 2, 4]
# x = 0
# for i in urutan:
#     x = x + 1
#     print("data ke ", x, "adalah = ", i)

# urutan = ["merah", "kuning", "hijau"]
# x = 0
# for j in urutan:
#     x = x + 1
#     print("data ke ", x, "adalah = ", j)

# for j in range (4, 8):
#     print(j)

# for k in range(1000, 10, -200):
#     print(k)

# genap = 0
# for i in range(1, 11):
#     genap = genap + 2
#     print("bilangan genap ke ", i, "adalah ", genap)

# ganjil = 1
# for i in range(1, 16):
#     ganjil = ganjil + 2
#     print("Bilangan ganjil ke ", i, "adalah ", ganjil)

# i = 5
# while i <= 5:
#     print("nilai saat ini", i)
#     i = i + 1
# print("=" * 55)

# total_belanja = int(input("Berapa total belanja Anda? "))
# member = str(input("Apakah Anda sudah menjadi member? "))
# if str(member) == "sudah":
#     if total_belanja >= 500000:
#         discount = 0.25
#         print("Anda akan mendapatkan diskon sebesar 25%")
#     elif total_belanja >= 100000:
#         discount = 0.2
#         print("Selamat Anda akan mendapatkan diskon sebesar 20%")
# else:
#     discount = 0.1
#     print("Anda akan mendapatkan diskon sebesar 10%")

# total = total_belanja - (total_belanja * discount)
# print("Jadi total belanja yang harus Anda bayar adalah sebesar ", total)

# list = ["mama", "ayah", "teteh", "mvs", "malebul", "geng dalem geng", "nadhira", "athalla", "kelasanjing"]
# print(list[6])

# list = ["mama", "ayah", "teteh", "mvs", "malebul", "geng dalem geng", "nadhira", "athalla", "kelasanjing"]
# print(list[6])
# print(list[0])
# print(len(list[2]))

# print("=" * 55)

# list = ["mama", "ayah", "teteh", "mvs", "malebul", "geng dalem geng", "nadhira", "athalla", "kelasanjing"]
# list.insert(5, "lica")
# print(list)

# print("=" * 55)

# kelas = ["ranti", "lica", "dea", "aurel", "audry", "lathifa", "angie", "chilya", "akila", "dzikra"]
# for i in range(len(kelas)):
#     print("urutan mahasiswa no absen", i+1, "adalah", kelas(i))

# matriksA = [[1, 2],
#             [3, 4]]
# print(matriksA)

# matriksA = [[1, 2], [3, 4]]
# print("bentuk pertama memanjang", matriksA)
# for x in range(0, len(matriksA)):
#     print()
#     for y in range(0, len(matriksA[0])):
#         print(matriksA[x][y], end=" ")
#     print()

# matriksA = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
# matriksB = [[10, 11, 12],
#             [13, 14, 15],
#             [16, 17, 18]]
# print("mulai menjumlah dua matriks: ")
# for x in range(0, len(matriksB)):
#     print()
#     for y in range(0, len(matriksB[0])):
#         print(matriksA[x][y] + matriksB[x][y], end=" ")
#     print()

# matriksA = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
# matriksB = [[10, 11, 12],
#             [12, 13, 14],
#             [15, 16, 17]]
# for x in range(0, len(matriksA)):
#     print()
#     baris = []
#     for y in range(0, len(matriksB[0])):
#         total = 0
#         for z in range(0, len(matriksA)):
#             total = total + (matriksA[x][z] * matriksB[z[y]])
#         baris.append(total)

# pelanggan = ["lathifa", "lica", "dea", "chilya"]
# alamat = ["jl. gagak", "jl. mega", "jl. sukoharjo", "jl. demak"]

# def masukpelanggan():
#     pelanggan_baru = input("Masukkan nama pelanggan: ")
#     pelanggan.append(pelanggan_baru)
#     alamat_baru = input("Masukkan alamat pelanggan: ")
#     alamat.append(alamat_baru)

# def tampilkanData():
#     for i in range(0, len(pelanggan)):
#         print("no", i+1, "nama pelanggan: ", f"{pelanggan[i]:<20}", "alamat: ", f"{alamat[i]}")
# jawaban = input("Apakah Anda ingin memasukkan data pelanggan (ya/tidak)? ")
# tampilkanData()

# pelanggan = ["lathifa", "lica", "dea", "chilya"]
# alamat = ["jl. gagak", "jl. mega", "jl. sukoharjo", "jl. demak"]

# def tampilkanData():
#     for i in range(0, len(pelanggan)):
#         print("no", i+1, "nama pelanggan: ", f"{pelanggan[i]:<20}", "alamat: ", f"{alamat[i]}")
# jawaban = input("Apakah Anda ingin memasukkan data pelanggan (ya/tidak)? ")
# tampilkanData()

# kilogram = int(input("Masukkan nilai dalam satuan kilogram: "))
# gram = kilogram * 1000
# print("input masukkan: {} kg".format(int(kilogram)))
# print("Hasil konservi: {} g".format(int(gram)))

# def sayang():
#     print("mama")
# sayang()
# sayang()
# sayang()

# tinggi = int(input("Masukkan nilai tinggi yang ingin Anda pakai: "))
# alas = int(input("Masukkan nilai alas yang ingin Anda pakai: "))
# luas_segitiga = 1/2 * alas * tinggi
# print("Jadi luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas_segitiga, "cm^2.")

# def faktorial(n):
#     if x <= 1:
#         return 1
#     else:
#         return x * faktorial(x - 1)
# angka = int(input("masukkan angka: "))
# angka = angka + 1
# for x in range(angka):
#     print("%d" % (x, faktorial(x)))

# # tipe rumah
# tipe_rumah = ['T45/84', 'T55/112', 'T60/120 (hook)']

# # harga rumah
# harga_rumah = [550_000_000, 850_000_000, 950_000_000]

# # uang muka (dalam persen)
# uang_muka = [0, 10, 20, 30]

# # suku bunga kredit
# suku_bunga = 0.06

# # rentang kredit (dalam tahun)
# rentang_kredit = range(5, 31)

# # fungsi untuk menghitung cicilan tetap per bulan
# def cicilan_tetap(uang_pinjaman, suku_bunga, rentang_kredit):
#     jml_bulan = rentang_kredit * 12
#     cicilan_bunga_bulanan = (suku_bunga * uang_pinjaman) / 12
#     cicilan_pokok_bulanan = uang_pinjaman / jml_bulan
#     cicilan_bulanan = cicilan_bunga_bulanan + cicilan_pokok_bulanan
#     return cicilan_bulanan

# # loop untuk menghitung uang pertama dan cicilan bulanan untuk setiap tipe rumah, uang muka, dan rentang kredit
# for i in range(len(tipe_rumah)):
#     print(f"{'='*30}\nTipe Rumah: {tipe_rumah[i]}\n{'-'*30}")
#     for j in range(len(uang_muka)):
#         print(f"Uang Muka: {uang_muka[j]}%")
#         for k in rentang_kredit:
#             uang_pinjaman = harga_rumah[i] * (100 - uang_muka[j]) / 100
#             cicilan_bulanan = cicilan_tetap(uang_pinjaman, suku_bunga, k)
#             uang_pertama = harga_rumah[i] * uang_muka[j] / 100
#             print(f"Rentang Kredit: {k} tahun")
#             print(f"Uang Pertama yang harus dibayarkan: {uang_pertama:,.0f} rupiah")
#             print(f"Cicilan Bulanan: {cicilan_bulanan:,.0f} rupiah\n")

# harga_rumah = int(input("Masukkan harga rumah yang akan dibeli: "))
# uang_muka = int(input("Masukkan jumlah uang muka yang ingin dibayar: "))
# jangka_waktu = int(input("Masukkan jangka waktu cicilan (antara 5-30 tahun): "))

# suku_bunga = 0.005
# utang = harga_rumah - uang_muka
# cicilan_bunga_bulanan = (suku_bunga * utang * jangka_waktu) / (jangka_waktu * 12)
# cicilan_pokok_bulanan = harga_rumah / (jangka_waktu * 12)
# total_cicilan_bulanan = cicilan_bunga_bulanan + cicilan_pokok_bulanan

# biaya_notaris = 2000000
# biaya_provisi = 1500000
# pajak_pembelian = 0.025 * harga_rumah
# pnbp = 650000
# biaya_balik_nama = 1500000

# total_pembayaran_pertama = uang_muka + biaya_notaris + biaya_provisi + pajak_pembelian + pnbp + biaya_balik_nama

# print("=====================REPORT I=====================")
# print(f"Besar hutang : Rp {utang}")
# print(f"Cicilan pokok bulanan : {cicilan_pokok_bulanan} / bulan")
# print(f"Cicilan bunga bulanan : {cicilan_bunga_bulanan} / bulan")
# print(f"Total cicilan setiap bulan : {total_cicilan_bulanan}")
# print("=====================REPORT II=====================")
# print(f"Uang muka : Rp {uang_muka}")
# print(f"Cicilan bulanan pertama: Rp {total_cicilan_bulanan}")
# print(f"Biaya notaris : Rp {biaya_notaris}")
# print(f"Biaya provisi : Rp {biaya_provisi}")
# print(f"Pajak pembelian : Rp {pajak_pembelian}")
# print(f"PNBP : Rp {pnbp}")
# print(f"Biaya balik nama : Rp {biaya_balik_nama}")
# print(f"Total pembayaran pertama : Rp {total_pembayaran_pertama}")

# print(
# '''Pilih type rumah yang diinginkan:
# A. T45/84
# B. T55/112
# C. T60/120 (hook)''')

# tipe_rumah = str(input("Masukkan tipe rumah yang akan dibeli (A/B/C): "))
# uang_muka = int(input("Masukkan uang muka yang ingin dibayar (dalam persen): "))
# jangka_waktu = int(input("Masukkan jangka waktu cicilan (antara 5-30 tahun): "))

# if tipe_rumah == "A":
#     harga_rumah = 550000000
# elif tipe_rumah == "B":
#     harga_rumah = 850000000
# elif tipe_rumah == "C":
#     harga_rumah = 950000000

# suku_bunga = 0.06
# jlh_uang_muka = (uang_muka / 100) * harga_rumah
# utang = harga_rumah - jlh_uang_muka
# cicilan_bunga_bulanan = (suku_bunga * utang * jangka_waktu) / (jangka_waktu * 12)
# cicilan_pokok_bulanan = harga_rumah / (jangka_waktu * 12)
# total_cicilan_bulanan = cicilan_bunga_bulanan + cicilan_pokok_bulanan

# biaya_notaris = 2000000
# biaya_provisi = 1500000
# pajak_pembelian = 0.025 * harga_rumah
# pnbp = 650000
# biaya_balik_nama = 1500000

# total_pembayaran_pertama = uang_muka + biaya_notaris + biaya_provisi + pajak_pembelian + pnbp + biaya_balik_nama

# print("=====================REPORT I=====================")
# print(f"Besar hutang : Rp {utang}")
# print(f"Cicilan pokok bulanan : {cicilan_pokok_bulanan} / bulan")
# print(f"Cicilan bunga bulanan : {cicilan_bunga_bulanan} / bulan")
# print(f"Total cicilan setiap bulan : {total_cicilan_bulanan}")
# print("=====================REPORT II=====================")
# print(f"Uang muka : Rp {jlh_uang_muka}")
# print(f"Cicilan bulanan pertama: Rp {total_cicilan_bulanan}")
# print(f"Biaya notaris : Rp {biaya_notaris}")
# print(f"Biaya provisi : Rp {biaya_provisi}")
# print(f"Pajak pembelian : Rp {pajak_pembelian}")
# print(f"PNBP : Rp {pnbp}")
# print(f"Biaya balik nama : Rp {biaya_balik_nama}")
# print(f"Total pembayaran pertama : Rp {total_pembayaran_pertama}")

for karakter in "imperiale":
    print(karakter)