#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <string>

using namespace std;

//Функции из задания
//Если передать q=1, то вернет результат функции для первого задания
//Если передать q=2, то вернет результат функции для второго задания
double func(double x, double y, int q)
{
    switch (q)
    {
    case 1:
        return x + cos(y / exp(1));
    
    case 2:
        return cos(1.5 + y) + x - y;
    }
}

//----------------------------//Adams//--------------------------//

void Adams(vector<vector<double>> &res, double x, double xn, double y, double h, int q)
{
    //Добавляем в массив начальные условия
    res.resize(2);
    res[0].push_back(x);
    res[1].push_back(y);

    //Переменные для расчета методом Рунге-Кутта
    double K1;
    double K2;
    double K3;
    double K4;

    //Вычисляем начальный отрезок методом Рунге-Кутта
    for (int i = 1; i < 4; i++)
    {
        K1 = func(x , y, q);
        K2 = func(x + h / 4.0, y + (h / 4.0) * K1, q);
        K3 = func(x + h / 2.0, y + (h / 2.0) * K2, q);
        K4 = func(x + h, y + h * K1 - 2.0 * h * K2 + 2.0 * h * K3, q);

        y = y + (h * (K1 + 2.0 * K2 + 2.0 * K3 + K4)) / 6.0;
        x += h;

        res[0].push_back(x);
        res[1].push_back(y);
    }

    //Вычисляем все остальные значения при помощи метода Адамса
    double df[3];
    for (int i = 4; i < 11; i++)
    {
        df[0] = res[1][i] - res[1][i - 1];
        df[1] = res[1][i] - 2.0 * res[1][i - 1] + res[1][i - 2];
        df[2] = res[1][i] - 3.0 * res[1][i - 1] + 3.0 * res[1][i - 2] - res[1][i - 3];

        y = y + h * func(x, y, q) + (df[0] * h * h / 2.0) + 5.0 * (df[1] * h * h * h / 12.0)
                + 3.0 * (df[2] * h * h * h * h / 8.0);
        x += h;

        res[0].push_back(x);
        res[1].push_back(y);
    }
    
}

//--------------------------//RungeKutt//---------------------------//

void RungeKutt(vector<vector<double>> &res, double x, double xn, double y, double h, int q)
{
    //Добавляем в массив начальные условия
    res.resize(2);
    res[0].push_back(x);
    res[1].push_back(y);

    double K1;
    double K2;
    double K3;
    double K4;

    //по формуле высчитываем все остальные точки
    while (x <= xn)
    {
        K1 = func(x , y, q);
        K2 = func(x + h / 4.0, y + (h / 4.0) * K1, q);
        K3 = func(x + h / 2.0, y + (h / 2.0) * K2, q);
        K4 = func(x + h, y + h * K1 - 2.0 * h * K2 + 2.0 * h * K3, q);

        y = y + (h * (K1 + 2.0 * K2 + 2.0 * K3 + K4)) / 6.0;
        x += h;

        res[0].push_back(x);
        res[1].push_back(y);
    }
}

//-----------------------------------//Euler//------------------------------//

void Euler(vector<vector<double>> &res, double x, double xn, double y, double h, int q)
{
    //Добавляем в массив начальные условия
    res.resize(2);
    res[0].push_back(x);
    res[1].push_back(y);

    //по формуле высчитываем все остальные точки
    while (x <= xn)
    {
        y = y + h * func(x, y, q);
        x += h;

        res[0].push_back(x);
        res[1].push_back(y);
    }
}

//-----------------------//EulerRecalculation//----------------------------//

void EulerRecalculation(vector<vector<double>> &res, double x, double xn, double y, double h, int q)
{
    double recalculationY;

    //Добавляем в массив начальные условия
    res.resize(2);
    res[0].push_back(x);
    res[1].push_back(y);

    //по формуле высчитываем все остальные точки
    int i = 1;
    while (x <= xn)
    {
        recalculationY = y + h * func(x, y, q);
        y = y + 0.5 * h * (func(x, y, q) + func(x, recalculationY, q));
        x += h;

        res[0].push_back(x);
        res[1].push_back(y);

        i++;
    }
}

//Функция вывода таблиц
void Print(const vector<vector<double>> &res)
{
    cout << "+-----------+-----------+\n";
    cout << "|     x     |     y     |\n";
    cout << "+-----------+-----------+\n";
    for (int i = 0; i < res[0].size(); i++)
    {
        cout << "|" << setw(11) << setprecision(5) << res[0][i] << "|" << setw(11) << setprecision(5) << res[1][i] << "|\n";
        cout << "+-----------+-----------+\n";
    }
}

//-----------------------------//main//---------------------------------------------//

int main()
{
    double x;
    double xn;
    double y;

    vector<vector<double>> vec;

    //------------------------//Задание 1//------------------------//

    cout << "//----------//Task 1//----------//\n\n";

    x = 1.4;
    xn = 2.4;   //Начальные условия для первой задачи
    y = 2.5;

    cout << "Euler:\n";
    Euler(vec, x, xn, y, 0.1, 1);
    Print(vec);
    vec.clear();

    cout << "Euler Recalculation:\n";
    EulerRecalculation(vec, x, xn, y, 0.1, 1);
    Print(vec);
    vec.clear();

    cout << "Runge-Kutt:\n";
    RungeKutt(vec, x, xn, y, 0.1, 1);
    Print(vec);
    vec.clear();


    //------------------------//Задание 2//------------------------//

    cout << "\n\n//----------//Task 2//----------//\n\n";

    x = 0;
    xn = 1;     //Начальные условия для второй задачи
    y = 0;

    cout << "Euler Recalculation:\n";
    EulerRecalculation(vec, x, xn, y, 0.1, 2);
    Print(vec);
    vec.clear();

    cout << "Adams:\n";
    Adams(vec, x, xn, y, 0.1, 2);
    Print(vec);
    vec.clear();

    return 0;
}