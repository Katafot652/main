import matplotlib.pyplot as plt
import numpy as np

# 1. Основи роботи з Matplotlib
print("--- 1. Побудова кількох функцій на одному полі ---")
x = np.arange(-10, 10.1, 0.1)
y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = x^2', color='blue', linestyle='-')
plt.plot(x, y2, label='y = sin(x)', color='red', linestyle='--')
plt.plot(x, y3, label='y = e^x', color='green', linestyle='-.')

plt.title('Графіки базових функцій')
plt.xlabel('Значення X')
plt.ylabel('Значення Y')
plt.legend()
plt.grid(True)
plt.ylim(-10, 100) # Обмеження для наочності через експоненту
plt.show()

# 2. Робота з графіками (Косинус)
print("--- 2. Налаштування графіка cos(x) ---")
x_cos = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y_cos = np.cos(x_cos)

plt.figure()
plt.plot(x_cos, y_cos, color='magenta', linestyle=':', linewidth=2)
plt.title('Графік y = cos(x)')
plt.grid(True)
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-1.5, 1.5)
plt.show()

# 3. Побудова декількох графіків на одній фігурі
print("--- 3. Використання subplot() ---")
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x_cos, np.sin(x_cos), 'r')
plt.title('y = sin(x)')

plt.subplot(1, 2, 2)
plt.plot(x_cos, np.cos(x_cos), 'b')
plt.title('y = cos(x)')

plt.subplots_adjust(wspace=0.3) # Коригування розташування
plt.show()

# 4. Побудова гістограми
print("--- 4. Гістограма нормального розподілу ---")
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title('Гістограма випадкових чисел')
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.show()

# 5. Побудова стовпчикової діаграми
print("--- 5. Стовпчикова діаграма ---")
cities = ['Київ', 'Львів', 'Одеса', 'Дніпро', 'Вінниця']
population = [2884, 721, 1015, 966, 370] # умовні дані

plt.figure()
plt.bar(cities, population, color='orange')
plt.title('Населення міст (тис. осіб)')
plt.xlabel('Місто')
plt.ylabel('Населення')
plt.show()

# 6. Побудова кругової діаграми
print("--- 6. Кругова діаграма ---")
plt.figure()
plt.pie(population, labels=cities, autopct='%1.1f%%', startangle=140)
plt.title('Розподіл населення між містами')
plt.legend(loc="best")
plt.show()