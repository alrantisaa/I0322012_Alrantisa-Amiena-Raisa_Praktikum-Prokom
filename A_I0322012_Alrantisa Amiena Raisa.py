tipe_rumah = ["T45/84", "T55/112", "T60/120 (hook)"]
harga_rumah_di_solo = [550000000, 850000000, 950000000]
uang_muka = [0, 10, 20, 30]
jangka_waktu = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
tipe_rumah_konsumen = input("Masukkan tipe rumah yang Anda inginkan: ")
harga_rumah_konsumen = int(input("Masukkan harga rumah yang Anda inginkan: "))
uang_muka_konsumen = int(input("Masukkan uang muka yang Anda ingin bayarkan: "))
jangka_waktu_konsumen = int(input("Masukkan jangka waktu yang Anda inginkan: "))
suku_bunga = 0.06
utang = int(harga_rumah_konsumen - uang_muka_konsumen)
cicilan_bunga_bulanan = (suku_bunga * utang * jangka_waktu_konsumen) / jangka_waktu_konsumen/12
cicilan_pokok_bulanan = harga_rumah_konsumen / (jangka_waktu_konsumen * 12)
total_cicilan_bulanan = cicilan_bunga_bulanan + cicilan_pokok_bulanan
biaya_notaris = 2000000
biaya_provisi = 1500000
pajak_pembelian = 0.025 * harga_rumah_konsumen
PNBP = 650000
biaya_balik_nama = 1500000

total_harga = uang_muka_konsumen + biaya_notaris + biaya_provisi + pajak_pembelian + PNBP + biaya_balik_nama

print("REPORT I")
print(f"Besar hutang: Rp {utang}")
print(f"Cicilan pokok bulanan: {cicilan_pokok_bulanan} / bulan")
print(f"Cicilan bunga bulanan: {cicilan_bunga_bulanan} / bulan")
print(f"Total cicilan setiap bulan: {total_cicilan_bulanan}")
print("REPORT I")

print("REPORT II")
print(f"Uang muka: Rp {uang_muka_konsumen}")
print(f"Cicilan bulanan pertama: Rp {total_cicilan_bulanan}")
print(f"Biaya notaris: Rp {biaya_notaris}")
print(f"Biaya provisi: Rp {biaya_provisi}")
print(f"Pajak pembelian: Rp {pajak_pembelian}")
print(f"PNBP: Rp {PNBP}")
print(f"Biaya balik nama: Rp {biaya_balik_nama}")
print(f"Total pembayaran pertama: Rp {total_harga}")
print("REPORT II")