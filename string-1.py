#kartu nama siswa

print("Kartu Nama Siswa")

#input user
nama_siswa = input("masukkan nama siswa : ")
asal_sekolah = input("masukkan asal sekolah siswa : ").capitalize()
hobi = input("masukkan hobi siswa (boleh lebih dari satu dipisahkan koma): ")

#program untuk memproses input data nama siswa
bagian_nama = nama_siswa.split()
nama_depan = bagian_nama[0].capitalize()
nama_belakang = bagian_nama[-1].upper()
jumlah_huruf = len(nama_siswa.replace(" ", ""))

#program untuk memproses input data hobi
jumlah_hobi = len(hobi.split(","))

per_hobi = hobi.split(",")
daftar_hobi = [hobi.strip().capitalize() for hobi in per_hobi]
daftar_hobi = "\n- ".join(daftar_hobi)

#output kartu nama siswa
print("===== KARTU NAMA SISWA =====")
print(f"Nama Siswa \t: {nama_depan} {nama_belakang}")
print(f"Nama Sekolah \t: {asal_sekolah}")
print(f"Jumlah Huruf Nama Siswa \t: {jumlah_huruf}")
print(f"Jumlah Hobi \t: {jumlah_hobi}")
print(f"Daftar Hobi \t: \n- {daftar_hobi}")
print("=============================")
#end of program
   
