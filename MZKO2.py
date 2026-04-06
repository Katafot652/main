import numpy as np

# 1. Транспонування матриць 
print("--- 1. Транспонування ---")
# Квадратна матриця (4,4)
matrix_44 = np.random.randint(1, 10, (4, 4))
transposed_44 = np.transpose(matrix_44)
print(f"Квадратна матриця (4,4):\n{matrix_44}")
print(f"Транспонована:\n{transposed_44}")

# Не квадратна матриця (2,5)
matrix_25 = np.random.randint(1, 10, (2, 5))
transposed_25 = matrix_25.T
print(f"\nМатриця (2,5):\n{matrix_25}")
print(f"Форма транспонованої: {transposed_25.shape}")

# 2. Добуток матриць 
print("\n--- 2. Добуток матриць ---")
m1 = np.random.randint(1, 5, (3, 2))
m2 = np.random.randint(1, 5, (2, 3))
dot_prod = np.dot(m1, m2)
matmul_prod = np.matmul(m1, m2)
print(f"Добуток (3,2) на (2,3) через np.dot:\n{dot_prod}")

# Квадратна матриця на вектор-стовпець
square_m = np.random.randint(1, 5, (3, 3))
vector_col = np.random.randint(1, 5, (3, 1))
vec_prod = np.dot(square_m, vector_col)
print(f"Добуток квадратної матриці на вектор:\n{vec_prod}")

# 3. Векторні операції 
print("\n--- 3. Векторні операції ---")
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(f"Скалярний добуток (vdot): {np.vdot(v1, v2)}")
print(f"Векторний добуток (cross): {np.cross(v1, v2)}")
print(f"Зовнішнє множення (outer):\n{np.outer(v1, v2)}")

# 4. Визначник та обернена матриця 
print("\n--- 4. Визначник та обернена матриця ---")
matrix_33 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
det = np.linalg.det(matrix_33)
print(f"Матриця (3,3):\n{matrix_33}")
print(f"Визначник: {det:.2f}")

if det != 0:
    inv_matrix = np.linalg.inv(matrix_33)
    print(f"Матриця невироджена. Обернена матриця:\n{inv_matrix}")
else:
    print("Матриця вироджена, оберненої не існує.")

# 5. Сортування та округлення 
print("\n--- 5. Сортування та округлення ---")
unsorted_arr = np.array([3.14159, 1.61803, 2.71828, 0.57721])
sorted_arr = np.sort(unsorted_arr)
rounded_arr = np.round(sorted_arr, 2)
print(f"Відсортований масив: {sorted_arr}")
print(f"Округлений (2 знаки): {rounded_arr}")

# 6. Обчислення функцій від масивів 
print("\n--- 6. Функції від масивів ---")
x = np.array([-5, 2, -10, 7, 0])
# Всі значення стають абсолютними
abs_arr = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])
print(f"Абсолютні значення (piecewise): {abs_arr}")

# Власна функція через vectorize
def my_func(val):
    return val ** 2 + 10

v_func = np.vectorize(my_func)
print(f"Результат vectorize (x^2 + 10): {v_func(x)}")

# 7. Кінцеві різниці та кумулятивна сума 
print("\n--- 7. Різниці та суми ---")
arr_sum = np.array([1, 2, 4, 7, 11])
print(f"Масив: {arr_sum}")
print(f"Кумулятивна сума (cumsum): {np.cumsum(arr_sum)}")
print(f"Різниця 1-го порядку (diff): {np.diff(arr_sum, n=1)}")
print(f"Різниця 2-го порядку (diff): {np.diff(arr_sum, n=2)}")