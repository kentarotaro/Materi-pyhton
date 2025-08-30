# berapa baris segitiga yang ingin dibuat
row = 5

# membuat for loop untuk kolom segitiga
for i in range(0, row):
    # membuat for loop untuk mengisi spasi pada awal segitiga -1 sebagai i = 0 (maks i = row - 1)
    for j in range(0, row - i - 1):
        print(" ", end="")
    # membuat for loop untuk mengisi bintang pada segitiga dengan i + 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")