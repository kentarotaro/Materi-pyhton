def tambah(*args):
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil
def kurang(*args):
    hasil = 0
    for angka in args:
        hasil -= angka
    return hasil
def kali(*args):
    hasil = 1
    for angka in args:
        hasil *= angka
    return hasil
def bagi(*args):
    hasil = args[0]
    for angka in args[1:]:
        hasil /= angka
    return hasil

