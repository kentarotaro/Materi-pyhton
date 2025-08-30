# casting tipe data

a = 10;
print("data : ", a, "tipe : ", type (a))

b = float(a)
c = complex(a)
d = str(a)
e = bool(a)

data = (b, c, d, e)
print("data : ", data, "tipe : ", type (data))

#float
a = 3.2;
print("data : ", a, "tipe : ", type (a))

b = int(a)
c = complex(a)
d = str(a)
e = bool(a)

data = (b, c, d, e)
print("data : ", data, "tipe : ", type (data))


#boolean
a = True;
print("data : ", a, "tipe : ", type (a))

b = float(a)
c = complex(a)
d = str(a)
e = int(a)

data = (b, c, d, e)
print("data : ", data, "tipe : ", type (data))

#string
a = "bebek";
print("data : ", a, "tipe : ", type (a))

e = bool(a)

data = (b, c, d, e)
print("data : ", data, "tipe : ", type (data))


# input data

p = bool(int(input("Masukkan data bolean : ")))

if p == False:
    print("benar")
else:
    print("salah")

