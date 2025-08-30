# Tipe data

#int
a = 10
print("data : ", a, "bertipe : ", type(a))

#float
b = 10.5
print("data : ", b, "bertipe : ", type(b))

#string
c = "ayam" 
print("data : ", c, "bertipe : ", type(c))

#boolean
d = True
print("data : ", True, "bertipe : ", type(True)) 

a = 1
print("data : ", a, "bertipe : ", type(a))


# tipe data khusus

#bilangan kompleks
e = complex(12, 13)
print("data : ", e, "bertipe : ", type(e))

# tipe data dari bahasa c
from ctypes import c_double
f = c_double(9.3)
print("data : ", f, "bertipe : ", type (f))
