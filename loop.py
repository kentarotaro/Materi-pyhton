#loop(for and while), continue, break, pass

#1. loop
print("for loop")
a = 1
for i in range(1, 10):
    print(i)

#2. while loop
print("\nwhile loop")
a = 2
while a < 10:
    a +=2
    print(a)

#3. continue
print("\ncontinue")
a = 3
while a < 10:
    a +=3
    if a % 2 == 0:
        print("True")
        continue
    print (a)

#4. pass
print("\npass")
a = 4
while a < 10:
    a += 4
    if a % 2 == 0:
        print("True")
        pass
    print(a)

#5. break
print("\nbreak")
a = 3
while a < 10:
    a += 3
    if a % 2 == 0:
        print("True")
        break
    print(a)

#membuat segitiga 
print("\nSegitiga")
bintang =  0
for i in range(1, 6):
    bintang += 1
    print("*"*bintang)

#ganjil segtiga
print("\nSegitiga Ganjil")
bintang = -1
for i in range(1, 6):
    bintang += 2
    print("*"*bintang)

#segitiga sama kaki
print("\nSegitiga Sama Kaki")
bintang = 0
for i in range(1, 21):
    bintang += 1
    bagan_kiri = (f"{' ' * (20 - bintang)}")
    bagan_kanan = (f"{'*' * (bintang * 2 - 1)}")
    print(bagan_kiri + bagan_kanan)