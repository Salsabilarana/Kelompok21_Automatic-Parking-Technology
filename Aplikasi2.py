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
