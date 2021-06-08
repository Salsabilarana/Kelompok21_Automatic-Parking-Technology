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
    elif lama_parkir <= 5 :
        total_yang_harus_dibayar = 6000+((lama_parkir-1)*2000)
    elif lama_parkir <= 12 :
        total_yang_harus_dibayar = 25000
    elif lama_parkir <= 24 :
        total_yang_harus_dibayar = 55000
    ##biaya parkir roda 4 jika sudah melewati 1 hari
    else :
        ###perhitungan jam hari yang sudah terlewati (misal membaca 4 jam pada 2 HARI 4 JAM)
        sub_lama_parkir = lama_parkir-(hari*24)
        ####perhitungan biaya jam parkir yang akan ditambah dengan banyaknya hari menginap
        if sub_lama_parkir <= 1:
            sub_hari = 6000
        elif sub_lama_parkir <= 5:
            sub_hari = 6000+((sub_lama_parkir-1)*2000)
        elif sub_lama_parkir <= 12:
            sub_hari = 25000
        elif sub_lama_parkir <= 24:
            sub_hari = 55000
        else :
            sub_hari = 50000
        ###total yang harus dibayar
        print(hari, "Hari Menginap + ", sub_lama_parkir, "Jam Parkir")
        print(hari*50000, "+", sub_hari)
        total_yang_harus_dibayar = hari * 50000+sub_hari

#BIAYA PARKIR RODA 6
else :
    if lama_parkir <= 1 :
        total_yang_harus_dibayar = 8000
    elif lama_parkir <= 5 :
        total_yang_harus_dibayar = 8000+((lama_parkir-1)*3500)
    elif lama_parkir <= 12 :
        total_yang_harus_dibayar = 35000
    elif lama_parkir <= 24 :
        total_yang_harus_dibayar = 70000
    else:
        total_yang_harus_dibayar = ((hari + 1) * 70000)
        ###perhitungan jam hari yang sudah terlewati (misal membaca 4 jam pada 2 HARI 4 JAM)
        sub_lama_parkir = lama_parkir - (hari * 24)
        ####perhitungan biaya jam parkir yang akan ditambah dengan banyaknya hari menginap
        if sub_lama_parkir <= 1:
            sub_hari = 8000
        elif sub_lama_parkir <= 5:
            sub_hari = 8000 + ((sub_lama_parkir - 1) * 3500)
        elif sub_lama_parkir <= 12:
            sub_hari = 35000
        elif sub_lama_parkir <= 24:
            sub_hari = 70000
        else:
            sub_hari = 70000
        ###total yang harus dibayar
        print(hari, "Hari Menginap + ", sub_lama_parkir, "Jam Parkir")
        print(hari * 70000, "+", sub_hari)
        total_yang_harus_dibayar = hari * 70000 + sub_hari

#MENAMPILKAN TOTAL HARGA PARKIR YANG HARUS DIBAYAR
print()
print("\033[1;32;40m Total Yang Harus Dibayar : RP", total_yang_harus_dibayar)
print("\033[1;32;40m Lama Parkir :",hitung_lama_parkir)
print("\033[1;32;40m Total Yang Harus Dibayar : RP", total_yang_harus_dibayar)

#scan qr code pembayaran
try:
    bayar = decode(Image.open('pembayaran.png'))
    setelah_bayar = 1
except:
    setelah_bayar = 0
#kondisi gerbang
if setelah_bayar == 1:
    palang = ("Palang Terbuka")
else:
    palang=("Mohon Bayar Terlebih Dahulu")
print()
#Palang Terbuka
print("             ", palang)
print()
