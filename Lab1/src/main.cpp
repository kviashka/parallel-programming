#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <random>
#include <string>

// Функция перемножения матриц через циклы
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

    std::cout << "Starting matrix multiplication for N = " << n << "..." << std::endl;

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

    // Сохраняем исходные матрицы во входную папку data
    saveMatrix("data/matrix_A.txt", A, n);
    saveMatrix("data/matrix_B.txt", B, n);

    auto start = std::chrono::high_resolution_clock::now();
    multiplyMatrices(A, B, C, n);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> elapsed = end - start;
    std::cout << "Done in " << elapsed.count() << " ms." << std::endl;

    // Сохраняем результат в папку result
    saveMatrix("result/matrix_C.txt", C, n);

    std::ofstream log("benchmark_log.txt", std::ios::app);
    log << n << "," << elapsed.count() << "\n";

    return 0;
}