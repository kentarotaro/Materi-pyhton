#pengenalan list

data = [1, 2, 3, 4, 5]
print(data)  

data_str = ["satu", "dua", "tiga", "empat", "lima"]
print(data_str)

data_bool = [True, False, True, False]
print(data_bool)

data_mixed = [1, "dua", True, 3.14]
print(data_mixed)

data_nested = [[1, 2], [3, 4], [5, 6]]
print(data_nested)

#list denan for
data_for = [i**2 for i in range(1, 10) if i % 2 == 0]
print(data_for)

data_for2 = [i for i in range(1, 10) if i % 2 != 0]
print(data_for2)


#manipulasi list
print("\n======= Manipulasi List ======\n")
data = [1, 2, 3, 4, 5]
data.append(6)  # Menambahkan elemen ke akhir list
print("Setelah append:", data)

print(data[0])  # Mengakses elemen pertama
print(data[-1])  # Mengakses elemen terakhir
data.insert(0, 0)  # Menyisipkan elemen di awal list
print("Setelah insert:", data)

#extend
data.extend([7, 8, 9])  # Menambahkan beberapa elemen sekaligus
print("Setelah extend:", data)

data.remove(3)  # Menghapus elemen tertentu
print("Setelah remove:", data)

#ubah data'
data[2] = 99 # Mengubah elemen 
print("Setelah mengubah elemen:", data)

data.pop()  # Menghapus elemen terakhir dan mengembalikannya
print("Setelah pop:", data)

data.clear()  # Menghapus semua elemen dari list
print("Setelah clear:", data)

# Mengurutkan list
data = [5, 2, 9, 1, 5, 6]
data.sort()  # Mengurutkan list secara ascending
print("Setelah sort:", data)

data.reverse()  # Membalik urutan list
print("Setelah reverse:", data)

# Menghitung jumlah elemen tertentu
data = [1, 2, 2, 3, 4, 4, 4]
print("Jumlah elemen 2:", data.count(2))
print("Jumlah elemen 4:", data.count(4))
print("Jumlah elemen 5:", data.count(5)) 
print("Jumlah elemen 1:", data.count(1))  # Tidak ada elemen 5, hasilnya 0
# Tidak ada elemen 5, hasilnya 0, artinya tidak ada elemen 5 dalam list, kenapa? kar

#copy list
data_copy = data.copy()  # Membuat salinan dari list
print("Salinan dari list:", data_copy)

#nested list
peserta_1 = ["Andi", 25, "Laki-laki"]
peserta_2 = ["Budi", 30, "Laki-laki"]
peserta_3 = ["Cici", 22, "Perempuan"]

data_peserta = [peserta_1, peserta_2, peserta_3]  # Nested list

for peserta in data_peserta:
    print(f"nama: {peserta[0]}, usia: {peserta[1]}, jenis kelamin: {peserta[2]}")

print(f"data peserta : {data_peserta[0][2]}")

data_copy = data_peserta.copy()  # Membuat salinan dari nested list
print("Salinan dari nested list:", data_copy)

#address
print("\n======= Alamat List =======\n")
print(hex(id(data_peserta)))  # Alamat dari list data
print(hex(id(data_copy)))  # Alamat dari salinan list data