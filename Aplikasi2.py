print("================APLIKASI 2===================")
#IMPORT WAKTU
from datetime import datetime as dtm
#IMPORT MODUL UNTUK READ BARCODE
from pyzbar.pyzbar import decode
from PIL import Image

#input data waktu parkir
##waktu masuk
data_waktu = open("waktu.txt", "r") # tanggal dan jam saat masuk
masuk_str1 = data_waktu.readline()
tgl_text = (masuk_str1)
waktu_masuk = dtm.strptime(tgl_text,'%d-%b-%Y %H:%M:%S') # konversi string ke date
##waktu keluar
saat_ini = dtm.now() # tgl dan jam saat ini
masuk_str2 = dtm.strftime(saat_ini,'%d-%b-%Y %H:%M:%S')
tgl_text = (masuk_str2)
waktu_keluar = dtm.strptime(tgl_text,'%d-%b-%Y %H:%M:%S') # konversi string ke date

#INPUT DATA KENDARAAN
data_tipe_kendaraan = open("tipekendaraan.txt", "r")
tipe_kendaraan = data_tipe_kendaraan.readline()

#MENGHITUNG LAMA PARKIR
hitung_lama_parkir = waktu_keluar - waktu_masuk
detik_lama_parkir = hitung_lama_parkir.total_seconds()
jam_lama_parkir = (detik_lama_parkir / 3600)
if jam_lama_parkir == float(jam_lama_parkir) :
    lama_parkir = int(jam_lama_parkir+1)
else :
    lama_parkir = int(jam_lama_parkir)
##menghitung lama parkir jika lebih dari 1 hari
hari1 = waktu_masuk
hari2 = waktu_keluar
total_hari = hari2 - hari1

hari = total_hari.days

#HASIL DATA YANG DIPEROLEH DARI SCAN
print("==========================================================")
print()
print("Tipe Kendaraan Anda : ", (tipe_kendaraan))
print("Waktu Masuk Anda : ", waktu_masuk)#, type(waktu_masuk))
print("waktu Keluar Anda : ", waktu_keluar)#, type(waktu_keluar))
print("Lama Parkir Anda : ", hitung_lama_parkir)
#######print("Lama Parkir Yang Harus Dibayar : ", lama_parkir,"Jam")
print()
print("==========================================================")

#BIAYA PARKIR RODA 2
if tipe_kendaraan == "Roda 2" :
    if lama_parkir <= 24 :
        total_yang_harus_dibayar = 3000
    else :
        total_yang_harus_dibayar = (hari * 25000)

#BIAYA PARKIR RODA 4
elif tipe_kendaraan == "Roda 4" :
    if lama_parkir <= 1 :
        total_yang_harus_dibayar = 6000
