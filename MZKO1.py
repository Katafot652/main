import numpy as np  # [cite: 7]

print("--- 1. Створення та основні властивості масивів ---") # [cite: 6]
# Створення масивів [cite: 8]
arr1 = np.array([1, 5, 10, 15, 20])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Виведення властивостей для кожного масиву [cite: 9]
for i, arr in enumerate([arr1, arr2, arr3], 1):
    print(f"Масив {i}D:")
    print(f"  Розмірність (ndim): {arr.ndim}")
    print(f"  Форма (shape): {arr.shape}")
    print(f"  Кількість елементів (size): {arr.size}")
    print(f"  Тип даних (dtype): {arr.dtype}")
    print(f"  Розмір елемента в байтах (itemsize): {arr.itemsize}\n")

# Створення специфічних масивів розміру (3,3) [cite: 10]
print("Масив zeros:\n", np.zeros((3, 3)))
print("Масив ones:\n", np.ones((3, 3)))
print("Масив full (з вісімками):\n", np.full((3, 3), 8))
print("Одинична матриця (eye):\n", np.eye(3))

print("\n--- 2. Операції індексування та зрізи ---") # [cite: 11]
# Масив (5,5) з випадкових чисел [10, 50] [cite: 12]
rand_arr = np.random.randint(10, 51, size=(5, 5))
print("Початковий масив (5x5):\n", rand_arr)

print("Другий рядок:", rand_arr[1, :]) # [cite: 14]
print("Третій стовпець:", rand_arr[:, 2]) # [cite: 15]
print("Зріз (рядки 2-4, стовпці 1-3):\n", rand_arr[1:4, 0:3]) # [cite: 16]
print("Всі парні елементи:", rand_arr[rand_arr % 2 == 0]) # [cite: 17]
print("Елементи більші за 30 (булеве індексування):", rand_arr[rand_arr > 30]) # [cite: 18]

print("\n--- 3. Зміна форми масиву ---") # [cite: 19]
# Масив з 12 елементів [cite: 20]
a = np.arange(12)
print("reshape (3,4):\n", a.reshape(3, 4)) # [cite: 20]
print("reshape (4,3):\n", a.reshape(4, 3)) # [cite: 20]
print("reshape (2,6):\n", a.reshape(2, 6)) # [cite: 20]

# Одновимірний масив [cite: 21]
reshaped = a.reshape(3, 4)
print("Flatten (одновимірний):", reshaped.flatten()) # [cite: 21]
print("Транспонований масив:\n", reshaped.T) # [cite: 22]

print("\n--- 4. Арифметичні операції ---") # [cite: 23]
A = np.array([10, 20, 30, 40, 50]) # [cite: 24]
B = np.array([1, 2, 3, 4, 5])     # [cite: 24]

print("A + B =", A + B) # [cite: 26]
print("A - B =", A - B) # [cite: 26]
print("A * B =", A * B) # [cite: 26]
print("A / B =", A / B) # [cite: 26]
print("A в ступені 2 =", np.power(A, 2)) # [cite: 27]
print("Скалярний добуток A та B:", np.dot(A, B)) # [cite: 28]

# Статистика для А [cite: 29, 30]
print(f"Статистика масиву А: Середнє={np.mean(A)}, Мін={np.min(A)}, Макс={np.max(A)}, Std={np.std(A):.2f}")

print("\n--- 5. Генерація випадкових чисел ---") # [cite: 31]
# Нормальний розподіл [cite: 32]
norm_arr = np.random.randn(4, 4)
print("Нормальний розподіл (4,4):\n", norm_arr)

# Випадкові цілі [5, 20] [cite: 33]
rand_int_arr = np.random.randint(5, 21, size=(3, 3))
print("Цілі числа (3,3):\n", rand_int_arr)

# Випадковий рядок [cite: 34]
idx = np.random.randint(0, 3)
print(f"Випадковий рядок (індекс {idx}):", rand_int_arr[idx, :])