import matplotlib.pyplot as plt
import os

# Создаем папку pic, если она еще не создана
os.makedirs("pic", exist_ok=True)

# Данные экспериментов для N = 1200 при разном числе потоков
threads = [1, 2, 4, 8]
times = [1.246, 0.655, 0.352, 0.320]
speedups = [t1 / t for t1, t in zip([times[0]] * len(times), times)]

# 1. График зависимости времени от числа потоков
plt.figure(figsize=(8, 5))
plt.plot(threads, times, marker='s', linestyle='-', color='#d9534f', linewidth=2, markersize=7, label='Время выполнения (сек)')
plt.title('Зависимость времени выполнения от числа потоков (N = 1200)', fontsize=11, fontweight='bold')
plt.xlabel('Количество потоков (Threads)', fontsize=10)
plt.ylabel('Время (сек)', fontsize=10)
plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("pic/measurements_omp_time.png", dpi=300)
plt.close()

# 2. График ускорения (Speedup)
plt.figure(figsize=(8, 5))
plt.plot(threads, speedups, marker='o', linestyle='-', color='#2ca02c', linewidth=2, markersize=7, label='Ускорение S(T)')
plt.plot(threads, threads, linestyle='--', color='gray', label='Идеальное ускорение')
plt.title('Ускорение параллельного алгоритма (OpenMP)', fontsize=11, fontweight='bold')
plt.xlabel('Количество потоков (Threads)', fontsize=10)
plt.ylabel('Ускорение (раз)', fontsize=10)
plt.xticks(threads)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("pic/measurements_omp_speedup.png", dpi=300)
plt.close()

print("Графики для Lab2 успешно созданы и сохранены в папку pic/!")