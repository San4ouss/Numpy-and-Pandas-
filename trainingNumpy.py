import math

import numpy as np

# s = list((1, 2, 3, 4))
# print(s)
# arr1 = np.array(s)
# print(arr1)
# for i in arr1:
#     print(i)

# a = np.array([[1, 2, 3], [4, 5, "6"]])
# a = np.zeros((2, 3))
# a = np.full((2, 3), "G")
# a = np.arange(0, 5, 2)
# a = np.array([1.5, 2.6, 3.2, 4.1, 5.5], dtype=float)
# b = a.astype(int)
#
# print(a)
# print(a.ndim)
# print(a.dtype)
# print(b)
# print(b.dtype)

# m1 = np.array([3, 5, 7])
# m2 = np.array([2, 5, 4])
# print(m1 > m2)
# print(m1 < m2)
# print(m1 == m2)

# lst = [1, 2, 3, 4, 5]
# l1 = lst[1:3]
# l1[1] = 15
# print(l1)
# print(lst)

# arr1 = np.array(np.arange(6))
# arr2 = np.array(np.arange(10, 16))
# arr3 = np.array(np.arange(10, 11))
# arr4 = np.array(np.arange(10, 20))
# print(arr1 + 1000)
# print(arr1 + arr2)
# print(arr1 + arr3)
# print(arr1 + arr4)

# print((arr1 / 115) * 100)
# print(arr1 * 100 / 115)

# arr = np.arange(4)
# print(arr[0:5])
# print(arr[-2:])
# arr[:3] = 0
# print(arr)

# lst = list(range(5))
# lst[:3] = (0, 0)
# print(lst)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# arr[0] = 0
# print(arr)

# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(lst[:][0])
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr[:, 0])
# print(arr[:2, :2])


# arr1 = np.array([5, 4, 3, 2, 1, 10])
# arr2 = np.array([3, 2, 7, 9, 11, 10])
# print(arr1 == arr2)
# print(arr1 > arr2)
# mask = arr1 > 5
# print(arr1[mask])

# mask = [True, False, False, False, False, True]
# print(arr1[mask])

# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
#   ]
#
# print([list(i) for i in list(zip(*lst))])

# print(round(None))

# m1 = np.arange(5)
# print(m1)
# print(list(m1))

# m1 = np.array([1, 2, 3])
# m2 = np.array([5, "6", 7.1])
# print(m2)
# print(np.maximum(m1, m2)

# m1 = np.array([4, -5, 6, 7, -8, 5, 2])
# m1 = np.array([2, -3, 4, -5, 6, 7, -8], [10, 20, 1, 5, -5, 0])
# print(m1.argmax())

# print(np.all(np.array([True, False, True])))
# print(np.sort(m1))
# m1.sort()
# print(m1)
# print(sorted(m1))

# print("".join(reversed("Python")))
# lst = [1, 5, 2, 3, 0, 11]
# lst.sort(reverse=True)
# print(lst)

# arr = np.array([670.99, 540.50, 799.01])
# mask = (arr % 1 * 100).astype(int) == 99
# print(mask.astype("int32"))
# print(mask)
#
# print(int(670.99 % 1 * 100) == 99)
#
# print(math.floor(670.99))
# print(round(670.99 % 1 * 100))
# print(type(arr))

# Z = np.array([1, 5, 6, 7, 0, 11])
# M = np.array([i for i in range(len(Z)) if Z[i] != 0])
# print(M)
# print(np.where(Z != 0))

m1 = np.zeros((3, 3))
m1[[0, 1, 2], [0, 1, 2]] = np.ones(3)
# np.fill_diagonal(m1, 1)
print(m1)

# Z = np.array([1, 2, 0, 0, 4, 0])
# print(min(Z), max(Z))
