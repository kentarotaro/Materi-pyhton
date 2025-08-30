#date and time

import datetime 

hari_ini = datetime.date.today()

#1
print("Hari ini adalah:", hari_ini)
#2
print(f"Hari ini adalah:{hari_ini.strftime('%A, %d %B %Y')}")

import datetime as dt

hari = dt.date(2007, 10, 3)

print("Tanggal:", hari)
print(f"hari ={hari:%A}")



#Soal 
#Sistem Pengingat aktifitas harian
print("======== Sistem Pengingat Aktifitas Harian ========")

#import datetime
import datetime as dt

#input user
nama_lengkap = input("Masukkan nama lengkap: ").title()

#proses data terkait kesalahan input waktu
try :
    waktu_sekarang = input("Masukkan waktu aktifitas (hh:mm): ")
    waktu_sekarang = dt.datetime.strptime(waktu_sekarang, "%H:%M").time()
except ValueError:
    print("Waktu tidak valid")
    exit()

#proses data untuk waktu aktifitas sisa tidur
sisa_waktu = dt.datetime.combine(dt.date.today(), dt.time(21, 0)) - dt.datetime.combine(dt.date.today(), waktu_sekarang)
if sisa_waktu < dt.timedelta(0):
    sisa_waktu = dt.timedelta(0)
sisa_waktu = str(sisa_waktu).split(":")
sisa_waktu = f"{int(sisa_waktu[0])} jam {int(sisa_waktu[1])} menit"

#proses data untuk waktu aktifitas
if waktu_sekarang < dt.time(12, 0):
    saran = "Saatnya belajar dengan semangat!"
elif dt.time(12, 0) <= waktu_sekarang < dt.time(17, 0):
    saran = "Waktunya istirahat sejenak dan makan siang."
elif dt.time(17, 0) <= waktu_sekarang < dt.time(21, 0):
    saran = "Manfaatkan waktu untuk review pelajaran atau hobi."
else:
    saran = "Sudah malam! Saatnya tidur."

#output sistem pengingat aktifitas harian
data_pengingat = f"""
=======  PENGINGAT AKTIFITAS ======
Nama Pengguna    : {nama_lengkap}
Waktu Sekarang   : {waktu_sekarang.strftime('%H:%M')}
Sisa Waktu Tidur : {sisa_waktu}
Saran Aktivitas  : {saran}
===================================
"""

# print data pengingat aktifitas harian
print(data_pengingat)


    
    