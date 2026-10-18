# Лабораторная работа №1: Последовательное перемножение квадратных матриц

## Задание
Написать программу на языке C/C++ для перемножения двух квадратных матриц.
- **Входные данные:** файлы, содержащие значения исходных матриц (`data/matrix_A.txt`, `data/matrix_B.txt`).
- **Выходные данные:** файл со значениями результирующей матрицы (`result/matrix_C.txt`), время выполнения, объем задачи.
- **Обязательна автоматизированная верификация** результатов вычислений с помощью стороннего ПО (Python / NumPy).
- **Важное примечание преподавателя:** в первой лабораторной работе распараллеливание не используется. Необходимо провести эксперименты для разных размеров матриц с ощутимым временем обработки ($200, 400, 800, 1200, 1600, 2000$), а отчёт дополнить таблицами и графиками.

---

## Ход работы

### 1. Реализация программы на C++

В соответствии с требованиями, умножение матриц реализовано классическим алгоритмом через вложенные циклы (`for`), без использования сторонних оптимизированных библиотек, так как в следующих лабораторных работах этот код будет распараллеливаться.

#### Код основной программы (`scr/main.cpp`):

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <random>
#include <string>

// Функция перемножения матриц через циклы (без сторонних библиотек)
void multiplyMatrices(const std::vector<std::vector<double>>& A, 
                      const std::vector<std::vector<double>>& B, 
                      std::vector<std::vector<double>>& C, int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            C[i][j] = 0.0;
            for (int k = 0; k < n; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Функция сохранения матрицы в файл
void saveMatrix(const std::string& filename, const std::vector<std::vector<double>>& matrix, int n) {
    std::ofstream out(filename);
    out << n << "\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            out << matrix[i][j] << (j == n - 1 ? "" : " ");
        }
        out << "\n";
    }
}

int main(int argc, char* argv[]) {
    int n = 400; // размер по умолчанию
    if (argc > 1) {
        n = std::stoi(argv[1]);
    }

    std::vector<std::vector<double>> A(n, std::vector<double>(n));
    std::vector<std::vector<double>> B(n, std::vector<double>(n));
    std::vector<std::vector<double>> C(n, std::vector<double>(n, 0.0));

    std::mt19937 rng(42);
    std::uniform_real_distribution<double> dist(1.0, 10.0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            A[i][j] = dist(rng);
            B[i][j] = dist(rng);
        }
    }

    saveMatrix("data/matrix_A.txt", A, n);
    saveMatrix("data/matrix_B.txt", B, n);

    auto start = std::chrono::high_resolution_clock::now();
    multiplyMatrices(A, B, C, n);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> elapsed = end - start;
    saveMatrix("result/matrix_C.txt", C, n);

    std::ofstream log("benchmark_log.txt", std::ios::app);
    log << n << "," << elapsed.count() << "\n";

    return 0;
}