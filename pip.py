#pip
#numpy
import numpy as np
vector_a = np.array([1, 2, 3, 4])
print(vector_a**2)

matrix_b = np.array([[1, 2 ], [4, 5]])
print(matrix_b**2)

zeros_c = np.zeros((2,2))#mewakili matriks 2x2 dengan nilai 0
print(zeros_c)

ones_d = np.ones((2,2))#mewakili matriks 2x2 dengan nilai 1
print(ones_d)

matrix_f = np.array([[5, 7], [5, 2]])

jumlah = matrix_b * matrix_f #penjumlahan matriks
print(jumlah)