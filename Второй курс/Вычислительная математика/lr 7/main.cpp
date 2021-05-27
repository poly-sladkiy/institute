#include <iostream>

using namespace std;

void Gauss(double (&matrix)[4][5], double (&p)[4]) {
    double a;
    double m[4][5]{0.0};
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 5; j++) {
            m[i][j] = matrix[i][j];
        }
    }

    a = m[0][0];  // Делим первую строку на коэффициент a11
    for (int i = 0; i < 5; i++) {
        m[0][i] = m[0][i] / a;
    }

    a = m[1][0];  // Вычитаем из второй строки первую, умноженную на коэффициент a21
    for (int i = 0; i < 5; i++) {
        m[1][i] = m[1][i] - a * m[0][i];
    }

    a = m[2][0];  // Вычитаем из третьей строки первую, умноженную на коэффициент a31
    for (int i = 0; i < 5; i++) {
        m[2][i] = m[2][i] - a * m[0][i];
    }

    a = m[3][0];  // Вычитаем из четвертой строки первую, умноженную на коэффициент a41
    for (int i = 0; i < 5; i++) {
        m[3][i] = m[3][i] - a * m[0][i];
    }

    a = m[1][1];  // Делим вторую строку на коэффициент a22
    for (int i = 1; i < 5; i++) {
        m[1][i] = m[1][i] / a;
    }

    a = m[2][1];  // Вычитаем из третьей строки вторую, умноженную на коэффициент а32
    for (int i = 1; i < 5; i++) {
        m[2][i] = m[2][i] - a * m[1][i];
    }

    a = m[3][1];  // Вычитаем из четвертой строки вторую, умноженную на коэффициент а42
    for (int i = 1; i < 5; i++) {
        m[3][i] = m[3][i] - a * m[1][i];
    }

    a = m[2][2];  // Делим третью строку на коффициент а33
    for (int i = 2; i < 5; i++) {
        m[2][i] = m[2][i] / a;
    }

    a = m[3][2];  // Вычитаем из четвертой строки третью, умноженню на коэффициент a43
    for (int i = 1; i < 5; i++) {
        m[3][i] = m[3][i] - a * m[2][i];
    }

    a = m[3][3];  // Делим четвертую строку на коэффициент а44
    for (int i = 2; i < 5; i++) {
        m[3][i] = m[3][i] / a;
    }

    p[3] = m[3][4];
    p[2] = m[2][4] - m[2][3] * p[3];
    p[1] = m[1][4] - m[1][2] * p[2] - m[1][3] * p[3];
    p[0] = m[0][4] - m[0][1] * p[1] - m[0][2] * p[2] - m[0][3] * p[3];
}

double function(double x, const double p[4]) {
    double f = x * x * x * x + p[0] * x * x * x + p[1] * x * x + p[2] * x + p[3];
    return f;
}


double bisection(double a, double b, double(&p)[4]) {
    double e = 0.001; // находим корень уравнения с заданной точностью
    double c;
    while (true) {
        c = (a + b) / 2;  // находим середину отрезка
        if (function(a, p) * function(c, p) < 0) { // определяем границы, где находится корень
            b = c;
        } else {
            a = c;
        }

        if (abs(function(c, p) < e)) {
            break;
        }
    }
    return c;
}


void multiplicationMatrix(double (&a)[4][5], double (&b)[4], double(&Y)[4]) { // Перемножаем матрицы
    for (int i = 0; i < 4; i++) {
        Y[i] = 0.0;
        for (int j = 0; j < 4; j++) {
            Y[i] += a[i][j] * b[j];
        }
    }
}


void vectorComputation(double (&M)[4][5], double(&Y)[4][5]) { // Считаем вектора Y
    double Y0[4] = {1.0, 0.0, 0.0, 0.0};
    double Y1[4]{0.0};
    double Y2[4]{0.0};
    double Y3[4]{0.0};
    double Y4[4]{0.0};
    multiplicationMatrix(M, Y0, Y1);
    multiplicationMatrix(M, Y1, Y2);
    multiplicationMatrix(M, Y2, Y3);
    multiplicationMatrix(M, Y3, Y4);
    for (int i = 0; i < 4; i++) { // Заносим вектора Y в общую матрицу
        Y[i][0] = Y3[i];
    }
    for (int i = 0; i < 4; i++) {
        Y[i][1] = Y2[i];
    }
    for (int i = 0; i < 4; i++) {
        Y[i][2] = Y1[i];
    }
    for (int i = 0; i < 4; i++) {
        Y[i][3] = Y0[i];
    }
    for (int i = 0; i < 4; i++) {
        Y[i][4] = -Y4[i];
    }
}

void calculationEigenvalues(double(&p)[4], double(&a)[4]) { // Считаем собственные числа матрицы
    double f1 = 0.0, f2;
    double x = -50.0;
    int j = 0;

    for (int i = 0; i < 100; i++) { // нахождим промежуток с корнями
        f2 = function(x, p);
        if (f1 * f2 < 0) { // Проверка на наличие корней
            a[j] = bisection(x - 1, x, p);
            j++;
        }
        x++;
        f1 = f2;
    }
    cout << "Собственные числа:" << endl;
    for (int i = 0; i < 4; i++) {
        cout << "lambda_" << i << ": " << a[i] << endl;
    }
    cout << endl;
}


void calculationEigenvectors(double (&Y)[4][5], double (&p)[4], double (&a)[4]) {
    cout << "Собственные вектора:" << endl;
    double q[5]{0.0};
    double X[4]{0.0};
    double temp[4]{0.0};
    for (int i = 0; i < 4; i++) {
        for (double & _q : q) {
            _q = 0.0;
        }
        q[0] = 1.0;
        for (int j = 1; j < 5; j++) { // Считаем вектор q по формуле
            q[j] = a[i] * q[j - 1] + p[j - 1];
        }
        for (double & _q : X) {
            _q = 0.0;
        }
        for (double & _q : temp) {
            _q = 0.0;
        }

        for (int j = 0; j < 4; j++) { // Считаем собственный вектор по формуле
            for (int k = 0; k < 4; k++) {
                X[k] += Y[k][j] * q[j];
            }
        }

        cout << endl << "V" << i + 1 << ":" << endl << "{\t";
        for (double x : X) {
                cout << x << ",\t";
        }
        cout << "}" << endl;
    }
}


int main() {
    double M[4][5] = {
            {2.,    1,      1.4,    0.5},
            {1,     1,      0.5,    1},
            {1.4,   0.5,    2,      1.2},
            {0.5,   1,      1.2,    0.5}};

    double Y[4][5]{};
    vectorComputation(M, Y); // Считаем вектора Y
    double p[4]{0.0};
    Gauss(Y, p);// Находим корни системы линейных уравнений
    double a[4]{0.0};
    calculationEigenvalues(p, a); // Считаем собственные числа
    calculationEigenvectors(Y, p, a); // Считаем собственные вектора
}