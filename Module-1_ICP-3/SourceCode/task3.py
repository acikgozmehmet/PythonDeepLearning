import numpy as np

# Using NumPy create random vector of size 15 having only Integers in the range 1-20.
a = np.random.randint(1, 21, 15)
print(f"Vector is: {a}\n")

# Then reshape the array to 3 by 5
a = a.reshape(3, 5)
print(f"2D array after reshape:\n {a}\n")

# Then replace the max in each row by 0
a[np.arange(len(a)), a.argmax(1)] = 0
print(f"2D array after replacement:\n {a}")


# Alternative solution with for-loop which is NOT the preferred solution in the ICP
# (n, u) = a.shape
# print(f"\nNumber of rows : {n}, and number of columns {u}")
# for i in range(n):
#     print(f"Row before update {b[i]}")
#     b[i] = np.where(b[i] == np.amax(b[i]), 0, b[i])
#     # alternative to the previous line
#     # b[i][b[i].argmax()] = 0
#     print(f"Row after update {b[i]} \n")
#print(f"Vector after setting max to 0:\n {b}")
