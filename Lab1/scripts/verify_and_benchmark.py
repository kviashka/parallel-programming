import subprocess
import time
import numpy as np
import os

sizes = [200, 400, 800, 1200, 1600, 2000]
results = []

os.makedirs("data", exist_ok=True)
os.makedirs("result", exist_ok=True)

print("Сборка проекта через CMake...")
os.makedirs("build", exist_ok=True)
subprocess.run(["cmake", "-S", "..", "-B", "build", "-DCMAKE_BUILD_TYPE=Release"], check=True)
subprocess.run(["cmake", "--build", "build", "--config", "Release"], check=True)

if os.path.exists("benchmark_log.txt"):
    os.remove("benchmark_log.txt")

exe_path = os.path.join("build", "matrix_mult")
if os.name == 'nt':
    exe_path = os.path.join("build", "Release", "matrix_mult.exe")

for n in sizes:
    print(f"Запуск для N = {n}...")
    subprocess.run([exe_path, str(n)], check=True)
    
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
    max_diff = np.max(np.abs(mat_c - expected_c))
    is_valid = max_diff < 1e-5
    print(f"Верификация N={n}: {'УСПЕШНО' if is_valid else 'ОШИБКА'} (разница: {max_diff})")
    
    with open("benchmark_log.txt", "r") as log_f:
        log_lines = log_f.readlines()
        last_entry = log_lines[-1].strip().split(",")
        time_ms = float(last_entry[1])
        
    results.append((n, time_ms, is_valid))

print("\nРезультаты теста:", results)