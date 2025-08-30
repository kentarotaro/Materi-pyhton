#membuat variabel
a = 10

print("nilai x = ", a) 

y = 27

print("nilai w = ", y)

juta10 = 20

print("z = ", juta10)

print("nilai x + w + z = ", a + y + juta10)

# Variabel hanya berlaku satu dalam prompt 
# Dan sifatya sudah universal

# Dalam suatu peternakan terdapat 2juta ayam 
# 5 juta bebek jika 1 juta ayam diambil untuk dijual
# berapa sisa ayam dan bebek di peternakan

ayam = 2000000
bebek = 5000000

print("jumlah hewan ternak sebelum dijual = ", ayam + bebek)

print("jumlah hewan ternak setelah dijual = ", ayam + bebek - 1000000)

# Operasi hitung dapat digunakan dalam print dengan memerhatikan assumsi

nilai = int(input("masukkan nilai (0-100): "))

if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")

# contoh lain

p = 3 
q = 7 

PxQ = int(input("jika p = 3, q = 7. maka berapa nilai dari PxQ masukkan jawaban yang benar: "))

if PxQ  == 21:
    print("pintar sekali")
else:
    print("ayo belajar lebih giat!!!")

# Latihan soal angka rahasia

angka_rahasia = 134

tebakan = int(input("Latihan soal, menebak angka rahasia dengan setiap angka berbeda, kode rahasia memiliki 3 angka dengan angka pertama kurang dari angka kedua dan angka kedua kurang dari angka ketiga Apabila masing-masing angka dijumlah akan menghasilkan angka prima kurang dari 8: "))

if tebakan == angka_rahasia:
    print("benar")
else:
    print("salah")
