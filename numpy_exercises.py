import numpy as np

# 1. Broadcasting
A = np.array([[10, 20, 30], [40, 50, 60]])
B = np.array([1, 2, 3])
result_a = A + B
print(result_a)

C = np.array([[1, 2], [3, 4]])
D = np.array([10, 20])
result_b = C * D[:, np.newaxis]
print(result_b)

# 2. Indexing and Slicing
arr = np.arange(1, 25).reshape(2, 3, 4)

slice_a = arr[1]
print(slice_a)

slice_b = arr[:, :, -1]
print(slice_b)

slice_c = arr[::-1]
print(slice_c)

arr[arr % 2 == 0] = -1
print(arr)

# 3. np.repeat
arr = np.array([1, 2, 3, 4, 5, 6])

result_3a = np.repeat(arr[arr % 2 == 1], 2)
print(result_3a)

result_3b = np.repeat(arr, arr)
print(result_3b)

# 4. Normalizing
arr = np.array([10, 20, 30])
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized)

# 5. Bonus Challenge
matrix_3x3 = np.fromfunction(lambda i, j: i * j, (3, 3), dtype=int)
print(matrix_3x3)

matrix_4x4 = np.random.randint(1, 10, (4, 4))
np.fill_diagonal(matrix_4x4, 0)
print(matrix_4x4)


