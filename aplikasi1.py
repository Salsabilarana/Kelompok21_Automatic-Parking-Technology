print("================APLIKASI 1===================")
#IMPORT WAKTU
from datetime import datetime as dtm

#IMPORT MODULE UNTUK CREATE BARCODE
import pyqrcode

#MEMBUAT QR CODE UNTUK PEMBAYARAN
alat_bayar = pyqrcode.create("Terimakasih Telah Membayar")
alat_bayar.png('pembayaran.png', scale=8)

#kondisi gerbang
palang = "tutup"

#WAKTU MASUK
saat_ini = dtm.now() # tgl dan jam saat ini
waktu_masuk = dtm.strftime(saat_ini,'%d-%b-%Y %H:%M:%S')

#INPUT TIPE KENDARAAN
tipe_kendaraan = int(input("""
Tipe Ken3daraan
1. Roda 2
2. Roda 4
3. Roda 6
Masukan Angka : """))
if tipe_kendaraan == 1 :
    tipe_kendaraan = "Roda 2"
elif tipe_kendaraan == 2 :
    tipe_kendaraan = "Roda 4"
elif tipe_kendaraan == 3 :
    tipe_kendaraan = "Roda 6"
else :
    print("KENDARAAN TIDAK TERDAFTAR")
    
#WRITE DATA WAKTU
f = open("waktu.txt", "w")
f.write(waktu_masuk)
f.close()

#WRITE TIPE KENDARAAAN
f = open("tipekendaraan.txt", "w")
f.write(tipe_kendaraan)
f.close()
