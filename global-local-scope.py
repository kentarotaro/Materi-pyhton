#global and local scope

nama_global = "Global Variable"#ini merupakan variabel global

def fungsi():
    print("fungsi akan menampilkan", nama_global)
fungsi() #memanggil fungsi

#akses variabel global di dalam loop
for i in range(0,5):
    print("Loop ke-", i, "dengan nama global", nama_global)

#percabangan
if True:
    print("Ini adalah percabangan dengan nama global", nama_global)

##variable lokal
def fungsi_lokal():
    nama_lokal = "Local Variable"  # ini merupakan variabel lokal
fungsi_lokal()  # memanggil fungsi

##contoh penggunaan
nama_global = "Global Variable"  # ini merupakan variabel global
def fungsi_akses_lokal(a):
    global nama_global # mengakses variabel global
    nama_global = a  # ini merupakan variabel lokal
    print("Fungsi akan menampilkan", a)
fungsi_akses_lokal("Variabel Akses Lokal")  # memanggil fungsi

##contoh lain
angka = 0
for i in range(0, 5):
    angka += i  # ini merupakan variabel lokal
    angka_dummy = 0
print(angka)  # akan menampilkan hasil penjumlahan dari 0 sampai 4
print(angka_dummy)  # akan menampilkan 0 karena angka_dummy tidak diubah dalam loop
if True:
    angka_dummy = 10  # ini merupakan variabel lokal
print(angka)
print(angka_dummy)  # akan menampilkan 10 karena angka_dummy diubah dalam if

#kesimpulan
# Variabel global dapat diakses di dalam fungsi, loop, dan percabangan.
# Variabel lokal hanya dapat diakses di dalam fungsi atau blok kode tempat variabel tersebut didefinisikan dngan menggunakan tools global.
