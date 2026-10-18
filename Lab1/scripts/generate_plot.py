import matplotlib.pyplot as plt
import os

# Создаем папку pic, если она ещё не создана
os.makedirs("pic", exist_ok=True)

# Данные экспериментов (Размер N и среднее время в секундах)
sizes = [200, 400, 800, 1200, 1600, 2000]
times = [0.00425, 0.03412, 0.31580, 1.24550, 3.12045, 6.35020]

# Построение графика
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=6, label='Последовательный алгоритм O(N³)')

plt.title('Зависимость времени выполнения от размера матрицы N', fontsize=12, fontweight='bold')
plt.xlabel('Размер матрицы (N)', fontsize=10)
plt.ylabel('Время выполнения (сек)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()

# Сохранение графика в папку pic
output_path = "pic/measurements_seq.png"
plt.savefig(output_path, dpi=300)
print(f"График успешно создан и сохранен по пути: {output_path}")

# Показать график на экране (опционально)
plt.show()