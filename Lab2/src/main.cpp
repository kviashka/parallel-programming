#pragma omp parallel for

#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <random>
#include <string>
#include <omp.h>

// Параллельная функция умножения матриц с помощью OpenMP
void multiplyMatricesOMP(const std::vector<std::vector<double>>& A, 
                         const std::vector<std::vector<double>>& B, 
                         std::vector<std::vector<double>>& C, int n, int threads) {
    if (threads > 0) {
        omp_set_num_threads(threads);
    }

    #pragma omp parallel for collapse(2) schedule(static)
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            double sum = 0.0;
            for (int k = 0; k < n; ++k) {
                sum += A[i][k] * B[k][j];
            }
            C[i][j] = sum;
        }
    }
}

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
    int n = 400;
    int threads = 4; // Количество потоков по умолчанию

    if (argc > 1) n = std::stoi(argv[1]);
    if (argc > 2) threads = std::stoi(argv[2]);

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
    multiplyMatricesOMP(A, B, C, n, threads);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> elapsed = end - start;
    saveMatrix("result/matrix_C.txt", C, n);

    std::ofstream log("benchmark_omp_log.txt", std::ios::app);
    log << n << "," << threads << "," << elapsed.count() << "\n";

    return 0;
}