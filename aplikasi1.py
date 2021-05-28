print("================APLIKASI 1===================")
#IMPORT WAKTU
from datetime import datetime as dtm

#IMPORT MODULE UNTUK CREATE BARCODE
import pyqrcode

#MEMBUAT QR CODE UNTUK PEMBAYARAN
alat_bayar = pyqrcode.create("Terimakasih Telah Membayar")
alat_bayar.png('pembayaran.png', scale=8)
