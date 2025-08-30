##tutorial membaca file eksternal

print(3*"=", "membaca file txt", 3*"=")
file = open("C:/Users/Python practice/.vscode/data.txt", mode = "r")

#status
print(f"status read: {file.readable()}")
print(f"status write: {file.writable()}")

#print(file.read())
print(file.readline(), end="")#membaca baris pertama #mengubah \n menjadi str kosong    
print(file.readlines())#membaca semua baris

print(f"apakah file sudah di-close : {file.closed}")
file.close()
print(f"apakah file sudah di-close : {file.closed}") #fungsi close adalah untuk mencegah error file yang akan di-open berikutnya


##salah satu teknik membuka file di pyhton dengan with

print(3*"=", "membaca file txt dengan with", 3*"=")
with open("C:/Users/Python practice/.vscode/data.txt", mode = "r") as file:
    content = file.readline()
    print(content, end = "")
    print(f"apakah file sudah di-close : {file.closed}")

print(f"apakah file sudah di-close : {file.closed}") #sudah otomatis closed jika menggunakan with



##write
#1. mode write
with open("C:/Users/Python practice/.vscode/data.txt", mode = "w", encoding = "utf-8") as file:
    file.write("hai, im python") #over wirte atau mengganti isi file

#2. mode append 
with open("C:/Users/Python practice/.vscode/data.txt", mode = "a", encoding = "utf-8") as file:
    file.write("hai, for python")
with open("C:/Users/Python practice/.vscode/data.txt", mode = "a", encoding = "utf-8") as file: #mode append dengan mengubah w menjadi a
    file.write("hello for python")  

#3. mode r+
with open("C:/Users/Python practice/.vscode/data.txt", mode = "r+", encoding = "utf-8") as file:
    file.write("menambah dengan r+") #menimpa data sebelumnya pada baris awal sesuai dengan panjang data    
    data = file.read()
    print(data)