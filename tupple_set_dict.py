#tupple
a = (1, 2, 3, 5)
print(a[0])
#data tupple tidak bisa assigment
#contoh
#a[0] = 5 data akan menjadi error

#sets
b = {2, 3, 1, 0, 9, 8, 8}
print(b)
#set tidak dapat melakukan index dan bersifat himpunan

#dictionary
#sifat dictiory menggunakan key tidak array
c = {
    1 : "ayam",
    2 : "kucing",
    3 : a,
    4 : b
}

print(c[1])
print(c.get(1))
#untuk menambahkan data yang belum ada
c.update({5 : "wkwk"})
print(c)

#untuk menghapus data
del c[1]
print(c)

#loop dictionary
for key in c:
    print(key)#output yang keluar hanya key

#atau
kunci = c.keys()
print(kunci)
for key in c:
    print(c.get(key)) #ini yang keluar adala value

#atau untuk value
value = c.values()
print(value)

for value in c.values():
    print(value)

#items ini menampilkan keys and value
items = c.items()
print(items)

for items in c.items():
    print(items)

#cara mengambil pisah untuk key dan value menggunakan loop
print("="*8)
for key, value in c.items():
    print(f"key : {key}, value : {value}")

#copy dictionary
d = c
print(d)

#jika pake copy hasil dari assigment akan berbeda
d = c.copy()
c[1] = "kambing"#sifatnya append karena tidak ada key 1
print(c)
print(d)

#pop dictionary
print("==="*8)
e = d.pop(2)#ini akan mentransfer value and key dari data d = c ingat bahw key 1, maka dari itu  hanya ada di c karena tidak terassigment ke d
print (e) 
print (d)

#popitem dictionary
f = d.popitem() #popitem berfungsi khusus untuk data terakhir yaitu key and value-nya
print(f)



print(8*"====")
#multi keys dictionary
import datetime
dt_1 = {
    1 : "ayam",
    2 : "kucing",
    3 : a,
    4 : b, 
    5 : datetime.datetime(2000,9,9)
}

dt_2 = {
    1 : "babi",
    2 : "bebek",
    3 : c,
    4 : d,
    5 : datetime.datetime(2001, 8, 3)
}

dt_3 = {
    1 : "anjing",
    2 : "monyet",
    3 : e,
    4 : f,
    5 : datetime.datetime(2002, 6, 5)
}

a = {
    0 : dt_1,
    1 : dt_2,
    2 : dt_3
}

print(a)

for data in a:
    KEY = data
    Nama = a[KEY][1]
    Nama_2 = a[KEY][2]
    Nama_3 = a[KEY][3]
    Nama4 = a[KEY][4]
    Nama5 = a[KEY][5]
print(KEY, Nama, Nama_2, Nama_3, Nama4, Nama5)