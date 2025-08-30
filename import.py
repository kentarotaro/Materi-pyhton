#import
#berfungsi untuk mengambil program dari eksternal

#1 untuk menyambung program dari eksternal
#contoh
# import aritmatika

#2 import dengan data atau fungsi tertentu
#contoh
#import aritmatika
# print(aritmatika.tambah(5, 3))  # Output: 8
#jadi apabila mnyertakan data jangan lupa untuk menaruh name space pada file yang diimp

#import counter untuk menghitung jumlah kemunculan elemen dalam list lebih efisien

from collections import Counter
data = ["a", "b", "c", "a", "b", "a", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
data_count = Counter(data)
print(f"nilai a = {data_count['a']}")

#import io


'''
import sys
import cv2

# Double the backslashes
image_path = "C:/Users/Python practice/img/2b_littlekycap/WhatsApp Image 2024-06-22 at 10.52.31.jpeg"

img = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img is None:
    print(f"Error: Could not load image at {image_path}. Check if the file exists and the path is correct.")
    sys.exit()

while True:
    cv2.imshow(image_path, img)
    key = cv2.waitKey(0)
    if key == 27:
        break

cv2.destroyAllWindows()
sys.exit()
'''