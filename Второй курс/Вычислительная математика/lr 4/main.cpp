#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <thread>
#include <chrono>

#include "colors.h"
#include "logo.h"

using namespace poly::color;
using namespace std;

double a{0.8}, b{1.6};
int n1{8}, n2{20};
double h1{(b - a) / n1}, h2{(b - a) / n2};

vector<double> h1_iter = {};
vector<double> h1_func = {};
vector<double> h1_iter_minus_half = {};
vector<double> h1_func_minus_half = {};

vector<double> h2_iter = {};
vector<double> h2_func = {};
vector<double> h2_iter_minus_half = {};
vector<double> h2_func_minus_half = {};

double function(double x) {
    return log10(x * x + 1) / x;
}

void counting() {
    double tmp1{a};
    double tmp2{a};
    unsigned int i1{0};
    unsigned int i2{0};

    cout << "+-----+----------+----------+----------+----------+" << endl;
    cout << "|  i  |    xi    |    yi    |  xi-1/2  |  yi-1/2  |" << endl;
    cout << "+-----+----------+----------+----------+----------+" << endl;
    do {
        h1_iter.push_back(tmp1);
        h1_func.push_back(function(tmp1));
        tmp1 += h1;
        if (i1 == 0) {
            h1_iter_minus_half.push_back(0.0);
            h1_func_minus_half.push_back(0.0);
        } else {
            h1_iter_minus_half.push_back((h1_iter[i1 - 1] + h1_iter[i1]) / 2);
            h1_func_minus_half.push_back(function(h1_iter_minus_half[i1]));
        }
        cout << "| " << setw(3) << i1 << " | " << setw(8) << h1_iter[i1] << " | " << setw(8) << h1_func[i1] << " | "
             << setw(8) << h1_iter_minus_half[i1] << " | " << setw(8) << h1_func_minus_half[i1] << " | " << endl;
        i1++;
    } while (tmp1 <= b);
    cout << "+-----+----------+----------+----------+----------+" << endl << endl;

    cout << "+-----+----------+----------+----------+----------+" << endl;
    cout << "|  i  |    xi    |    yi    |  xi-1/2  |  yi-1/2  |" << endl;
    cout << "+-----+----------+----------+----------+----------+" << endl;
    do {
        h2_iter.push_back(tmp2);
        h2_func.push_back(function(tmp2));
        tmp2 += h2;
        if (i2 == 0) {
            h2_iter_minus_half.push_back(0.0);
            h2_func_minus_half.push_back(0.0);
        } else {
            h2_iter_minus_half.push_back((h2_iter[i2 - 1] + h2_iter[i2]) / 2);
            h2_func_minus_half.push_back(function(h2_iter_minus_half[i2]));
        }
        cout << "| " << setw(3) << i2 << " | " << setw(8) << h2_iter[i2] << " | " << setw(8) << h2_func[i2] << " | "
             << setw(8) << h2_iter_minus_half[i2] << " | " << setw(8) << h2_func_minus_half[i2] << " | " << endl;
        i2++;
    } while (tmp2 <= b);
    cout << "+-----+----------+----------+----------+----------+" << endl << endl;
}


double Rectangles1() {
    double I{0.0};

    for (double q : h1_func_minus_half) {
        I += q;
    }

    return I * h1;
}

double Rectangles2() {
    double I{0.0};

    for (double q : h2_func_minus_half) {
        I += q;
    }

    return I * h2;
}

double Trapezoids1() {
    double I{0.0};

    for (unsigned int q = 1; q < h1_func.size() - 1; q++) {
        I += h1_func[q];
    }

    return (I + (h1_func[0] + h1_func[h1_func.size() - 1]) / 2) * h1;
}

double Trapezoids2() {
    double I{0.0};

    for (unsigned int q = 1; q < h2_func.size() - 1; q++) {
        I += h2_func[q];
    }

    return (I + (h2_func[0] + h2_func[h2_func.size() - 1]) / 2) * h2;
}

double Simpson1() {
    double I{0.0};

    for (unsigned int q = 1; q < h1_func.size() - 1; q++) {
        if (q % 2 != 0) {
            I += 4 * h1_func[q];
        } else {
            I += 2 * h1_func[q];
        }
    }

    return (I + h1_func[0] + h1_func[h1_func.size() - 1]) * (h1 / 3);
}

double Simpson2() {
    double I{0.0};

    for (unsigned int q = 1; q < h2_func.size() - 1; q++) {
        if (q % 2 != 0) {
            I += 4 * h2_func[q];
        } else {
            I += 2 * h2_func[q];
        }
    }

    return (I + h2_func[0] + h2_func[h2_func.size() - 1]) * (h2 / 3);
}

int main() {
    cout << logotype << endl << endl;

    counting();

    double results[6][3] = {};

    // Итерации
    results[0][0] = 8;
    results[1][0] = 8;
    results[2][0] = 8;
    results[3][0] = 20;
    results[4][0] = 20;
    results[5][0] = 20;

    // Нумерация методов
    results[0][2] = 0;
    results[1][2] = 1;
    results[2][2] = 2;
    results[3][2] = 0;
    results[4][2] = 1;
    results[5][2] = 2;

    {
        auto start = chrono::system_clock::now();

        thread t1([&] { results[0][1] = Rectangles1(); });
        thread t2([&] { results[1][1] = Trapezoids1(); });
        thread t3([&] { results[2][1] = Simpson1(); });
        thread t4([&] { results[3][1] = Rectangles2(); });
        thread t5([&] { results[4][1] = Trapezoids2(); });
        thread t6([&] { results[5][1] = Simpson2(); });

        t1.join();
        t2.join();
        t3.join();
        t4.join();
        t5.join();
        t6.join();

        auto end = chrono::system_clock::now();
        chrono::duration<double> diff = end - start;
        cout << "Time to calculate all methods: " << setw(9)
             << diff.count() << " s." << endl;
    }

    for (int q = 0; q < 5; q++) {
        for (int i = 0; i < 5; i++) {
            if (results[i][1] > results[i + 1][1]) {
                swap(results[i][0], results[i + 1][0]);
                swap(results[i][1], results[i + 1][1]);
                swap(results[i][2], results[i + 1][2]);
            }
        }
    }

    cout << GREEN;

    cout << "+----------+-----+--------------------+" << endl;
    cout << "|  " << RED << "Result" << GREEN << "  |  "
         << RED << "n" << GREEN << "  |       "
         << RED << "Method" << GREEN << "       |" << endl;
    cout << "+----------+-----+--------------------+" << endl;

    for (auto &result : results) {
        cout << "| " << PURPLE << setw(8) << result[1] << GREEN
             << " | " << WHITE << setw(3) << result[0] << GREEN << " | ";
        if (result[2] == 0) {
            cout << CYAN << "Central rectangles" << GREEN << " |" << endl;
        }
        if (result[2] == 1) {
            cout << CYAN << "     Trapezoid    " << GREEN << " |" << endl;
        }
        if (result[2] == 2) {
            cout << "     " << CYAN << "Simpson's" << GREEN << "     |" << endl;
        }
        cout << "+----------+-----+--------------------+" << endl;
    }

    cout << RESET;

    return 0;
}