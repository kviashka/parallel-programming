import subprocess
import time
import numpy as np
import os

sizes = [200, 400, 800, 1200, 1600, 2000]
thread_counts = [1, 2, 4, 8]

os.makedirs("data", exist_ok=True)
os.makedirs("result", exist_ok=True)

print("Сборка OpenMP проекта через CMake...")
os.makedirs("build", exist_ok=True)
subprocess.run(["cmake", "-S", "..", "-B", "build", "-DCMAKE_BUILD_TYPE=Release"], check=True)
subprocess.run(["cmake", "--build", "build", "--config", "Release"], check=True)

if os.path.exists("benchmark_omp_log.txt"):
    os.remove("benchmark_omp_log.txt")

exe_path = os.path.join("build", "matrix_mult_omp")
if os.name == 'nt':
    exe_path = os.path.join("build", "Release", "matrix_mult_omp.exe")

for n in sizes:
    for t in thread_counts:
        print(f"Запуск: N = {n}, Потоков = {t}...")
        subprocess.run([exe_path, str(n), str(t)], check=True)
        
        # Верификация через NumPy (для N=500 или выборочно, чтобы не тратить много времени)
        if n <= 800:
            with open("data/matrix_A.txt", "r") as f:
                lines = f.readlines()
                mat_a = np.array([[float(x) for x in line.split()] for line in lines[1:]])
            with open("data/matrix_B.txt", "r") as f:
                lines = f.readlines()
                mat_b = np.array([[float(x) for x in line.split()] for line in lines[1:]])
            with open("result/matrix_C.txt", "r") as f:
                lines = f.readlines()
                mat_c = np.array([[float(x) for x in line.split()] for line in lines[1:]])
                
            expected_c = np.dot(mat_a, mat_b)
            if not np.allclose(mat_c, expected_c, rtol=1e-4, atol=1e-4):
                print(f"ОШИБКА верификации при N={n}, потоков={t}!")
            else:
                print(f"Верификация N={n}, потоков={t}: УСПЕШНО")

print("Бенчмарк OpenMP завершен успешно!")