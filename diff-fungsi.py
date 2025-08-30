# materi fungsi(diff)

# def str
def hello_world():
    print("Hello, World!")
hello_world()#akan menampilkan y pada fugsi hello world, atau peran hello wolrd sebagai f(x)

#fungsi dengan argument/parameter
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # akan menampilkan "Hello, Alice!"

#fungsi tambah dua angka
def tambah(a, b):
    hasil = a + b
    print(f"Hasil penjumlahan {a} + {b} = {hasil}")
tambah(5, 3)  # akan menampilkan "Hasil penjumlahan 5 + 3 = 8"


#fungsi dengan list str
def tampilkan_daftar(nama_list):
    for peserta in nama_list:
        print(f"Peserta: {peserta}")

peserta = ["Alice", "Bob", "Charlie"]
tampilkan_daftar(peserta)  # akan menampilkan daftar peserta

#bandingkan dengan variabel copy
def tampilkan_daftar(nama_list):
    finalis = nama_list.copy()  # membuat salinan dari nama_list denga tujuan tidak mengubah output dari fungsi
    for peserta in finalis:
        print(f"Peserta: {peserta}")

peserta = ["rubychan","anachan","sakurachan"]
tampilkan_daftar(peserta)  # akan menampilkan daftar peserta


print("\n\n====== Fungsi dengan Return Value ======\n\n")
#fungsi dengan return value(kembalian)
def hitung_luas_persegi(sisi):
    return sisi * sisi  # mengembalikan luas persegi
print(f"Luas persegi dengan sisi 5 adalah {hitung_luas_persegi(5)}")  # akan menampilkan "Luas persegi dengan sisi 5 adalah 25"

#fungsi dengan return banyak nilai
def hitung_luas_dan_keliling_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling  # mengembalikan dua nilai
print(f"Luas dan keliling persegi dengan sisi 5 adalah {hitung_luas_dan_keliling_persegi(5)}")  # akan menampilkan "Luas dan keliling persegi dengan sisi 5 adalah (25, 20)"
luas, keliling = hitung_luas_dan_keliling_persegi(5)
print(f"Luas: {luas}, Keliling: {keliling}")  # akan menampilkan "Luas: 25, Keliling: 20"

#latihan soal evaluasi nilai dengan fungsi
def evaluasi_nilai(nilai):
    try:
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 dan 100")
        elif 90 <= nilai <= 100:
            return "sangat baik"
        elif 75 <= nilai < 90:
            return "baik"
        elif 60 <= nilai < 75:
            return "cukup"
        else:
            return "perlu bimbingan"
    except ValueError as e:
        return str(e)

#default argument
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

print(greet_with_default("ayam"))  # akan menampilkan "Hello, ayam"

print("\n\n====== latihan fungsi-1 ======\n\n")
'''''
#latihan fungsi-1
import os
#membuat header program
os.system("cls")
print(f"{'program menghitung luas dan keliling persegi panjang:':^40}")
print("="*40)
#input
lebar = int(input("masukkan lebar persegi panjang: "))
panjang = int(input("masukkan panjang persegi panjang: "))
#program
luas = lebar * panjang
keliling = 2 * (lebar + panjang)
#output 
print(f"luas dan keliling persegi panjang dengan lebar {lebar} dan panjang {panjang} adalah {luas} m^2 dan {keliling} m")
'''''

'''''
#fungsi header program
def header():
    import os
    #membuat header program
    os.system("cls")
    print(f"{'program menghitung luas dan keliling persegi panjang:':^40}")
    print("="*40)

def input_user():
    #input
    lebar = int(input("masukkan lebar persegi panjang: "))
    panjang = int(input("masukkan panjang persegi panjang: "))
    return lebar, panjang
def hitung_luas_keliling(lebar, panjang):
    #program
    luas = lebar * panjang
    keliling = 2 * (lebar + panjang)
    return luas, keliling
def output(luas, keliling):
    #output 
    if opsi == '1':
        print(f"luas persegi panjang adalah {luas} m^2")
    elif opsi == '2':
        print(f"keliling persegi panjang adalah {keliling} m")
    elif opsi == '3':
        print(f"luas dan keliling persegi panjang adalah {luas} m^2 dan {keliling} m")
    
    
    print("="*40)
#main program
while True:
    header()
    opsi = input("apakah anda ingin menghitung luas atau keliling persegi panjang? (1/2/3): ").lower()
    if opsi not in ['1', '2', '3']:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        continue
    lebar, panjang = input_user()
    luas, keliling = hitung_luas_keliling(lebar, panjang)
    output(luas, keliling)

    

    iscontinue = input("apakah anda ingin menghitung luas dan keliling persegi panjang? (y/n): ").lower()
    if iscontinue == 'n':
        break
print("terima kasih telah menggunakan program ini")
'''''

#fungsi hynt
print("\n\n====== Fungsi HINT ======\n\n")
def fungsi_hint(argument:int) -> int:
    output = argument * 2
    return output
print(f"Output dari fungsi_hint dengan argumen 5 adalah {fungsi_hint(5)}")  # akan menampilkan "Output dari fungsi_hint dengan argumen 5 adalah 10

#args fungsi
def fungsi(*args):#fungsi dari args sendiri adalah untuk menerima argumen dalam bentuk list, jadi sebanyak apapun variabel dengan indeks akan tetap bisa diterima
    nama = args[0]
    umur = args[1]
    kelamin = args[2]
    print(f"Nama: {nama}, Umur: {umur}, Kelamin: {kelamin}")

fungsi("Alice", 30, "Perempuan")  # akan menampilkan "Nama: Alice, Umur: 30, Kelamin: Perempuan"

#kwargs fungsi
def nama(**kwargs):  # kwargs digunakan untuk menerima argumen dalam bentuk dictionary
    print(kwargs["nama"])#output keluaran akan menghasilkan dict yang mengarah pada key "nama"
nama(nama="Alice", umur=30, kelamin="Perempuan")  # akan menampilkan "Alice"

#fungi lambda
pangkat = lambda num, exp: num ** exp  # fungsi lambda untuk menghitung pangkat
print(f"2 pangkat 3 adalah {pangkat(2, 3)}")  # akan menampilkan "2 pangkat 3 adalah 8"

data_angka = [1, 2, 3, 4, 5]
data_angka_baru = list(filter(lambda x: x % 2 == 0, data_angka))  # menggunakan filter dengan lambda untuk mendapatkan angka genap
print(f"Angka genap dari {data_angka} adalah {data_angka_baru}")  # akan menampilkan "Angka genap dari [1, 2, 3, 4, 5] adalah [2, 4]"

#anonymous function
#currying -> haskell curying
def pangkat(n):
    return lambda x:x ** n  # mengembalikan fungsi lambda yang menghitung pangkat
pangkat_2 = pangkat(2)  # membuat fungsi untuk menghitung kuadrat
print(f"3 pangkat 2 adalah {pangkat_2(3)}")  # akan menampilkan "3 pangkat 2 adalah 9"
print(f"pangkat bebas : {pangkat(3)(4)}")  # akan menampilkan "pangkat bebas : 64" (4 pangkat 3)