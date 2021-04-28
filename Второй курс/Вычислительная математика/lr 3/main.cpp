#include <iostream>
#include <iomanip>
#include <vector>

#include "colors.h"
#include "logo.h"

using namespace std;
using namespace poly::color;

///////////////////////////////////////////////////////////////

//Исходные данные
vector<vector<float>> coord = {
        {0.15, 4.4817},
        {0.16, 4.9530},
        {0.17, 5.4739},
        {0.18, 6.0496},
        {0.19, 6.6859},
        {0.20, 7.3891},
        {0.21, 8.1662},
        {0.22, 9.0250},
        {0.23, 9.9742},
        {0.24, 11.0232},
        {0.25, 12.1825},
        {0.26, 13.4637},
        {0.27, 13.5123}
};

vector<float> argVal = {0.166, 0.266, 0.277, 0.144, 0.22};

vector<vector<float>> coordLagUneq = {
        {0.43, 1.63597},
        {0.48, 1.73234},
        {0.55, 1.87686},
        {0.62, 2.03345},
        {0.70, 2.22846},
        {0.75, 2.35973}
};

vector<float> argValLagUneq = {0.512, 0.441};

///////////////////////////////////////////////////////////////

//Получение факториала числа
int getFact(int n) {
    int res = 1;

    while (n > 1) {
        res *= n;
        n--;
    }

    return res;
}

///////////////////////////////////////////////////////////////

//Вывод конечных разностей в лестничном виде
void printNewton(vector<vector<float>> &finiteDifferences) {
    for (int i = 0; i < finiteDifferences.size(); i++) {
        if (i < 9) {
            cout << "Finite difference  " << (i + 1) << " order: ";
        } else {
            cout << "Finite difference " << (i + 1) << " order: ";
        }

        for (int j = 0; j < finiteDifferences[i].size(); j++) {
            cout << "|" << setw(11) << setprecision(5) << finiteDifferences[i][j] << " ";
        }
        cout << endl;
    }
}

///////////////////////////////////////////////////////////////

//Вычисление приближенного значения функции при интерполяции вперед
float directInterpolation(float t, vector<vector<float>> &coord, vector<vector<float>> &finiteDifferences) {
    float res = 0.0;

    //К результату прибавляются y0 + t*dy0

    res += coord[0][1];
    res += t * finiteDifferences[0][0];

    //Вычисление членов
    for (int i = 1; i < finiteDifferences.size(); i++) {
        float temp = 1.0;

        //Промежуточные вычисления знаменателя
        for (int j = 1; j <= i; j++) {
            temp *= (t - j);
        }

        //К текущему результату добавляем член вида: (t(t-1)..(t-n+1) * ΔnY0)/n!
        res += temp * t * finiteDifferences[i][0] / getFact((i + 1));
    }

    return res;
}

///////////////////////////////////////////////////////////////

//Вычисление приближенного значения функции при интерполяции назад
float reverseInterpolation(float t, vector<vector<float>> &coord, vector<vector<float>> &finiteDifferences) {
    float res = 0.0;

    //К результату прибавляются yn + t*dy(n-1)
    res += coord[coord.size() - 1][1];
    res += t * finiteDifferences[0][(finiteDifferences[0].size() - 1)];

    //Вычисление членов
    for (int i = 1; i < finiteDifferences.size(); i++) {
        float temp = 1.0;

        //Промежуточные вычисления знаменателя
        for (int j = 1; j <= i; j++) {
            temp *= (t + j);
        }

        //К текущему результату добавляем член вида: (t(t+1)..(t+n-1) * ΔnY(n-1))/n!
        res += t * temp * finiteDifferences[i][(finiteDifferences[i].size() - 1)] / getFact((i + 1));
    }

    return res;
}

///////////////////////////////////////////////////////////////

/*
############
##-Newton-##
############
*/

//Метод Ньютона
int Newton() {
    cout << PURPLE << "+-----Newton-----+\n" << RESET;

    vector<float> result;

    vector<vector<float>> finiteDifferences;

    //Хранение промежуточных значений
    vector<float> tempList;

    for (int i = 0; i < coord.size() - 1; i++) {
        //Вычисление конечных разностей
        tempList.push_back(coord[i + 1][1] - coord[i][1]);
    }

    finiteDifferences.push_back(tempList);
    tempList.clear();

    //На каждом i-ом шаге вычисляем значения конченых разностей нового порядка
    for (int i = 0; i < coord.size() - 2; i++) {
        for (int j = 0; j < finiteDifferences[i].size() - 1; j++) {
            //Вычисление конечных разностей
            tempList.push_back(finiteDifferences[i][j + 1] - finiteDifferences[i][j]);
        }
        finiteDifferences.push_back(tempList);
        tempList.clear();
    }

    printNewton(finiteDifferences);

    //Вычисление шага h
    float h = coord[1][0] - coord[0][0];

    float t;

    //Вычисление середины отрезка переданных X
    float midPoint = (coord[0][0] + coord[coord.size() - 1][0]) / 2;

    //Находим значения функции
    for (int k = 0; k < argVal.size(); k++) {
        //Если Xi лежит в промежутке [x0; (x0 + xn) / 2]
        if (argVal[k] < midPoint) {
            //t вычисляется как (x - x0)/h
            t = (argVal[k] - coord[0][0]) / h;

            //В список ответов заносим значение полученное при интерполяции вперед
            result.push_back(directInterpolation(t, coord, finiteDifferences));
        }
            //Иначе Xi лежит в промежутке [(x0 - xn)/2; xn]
        else {
            //t вычисляется как (x - xn)/h
            t = (argVal[k] - coord[coord.size() - 1][0]) / h;

            //В список ответов заносим значение полученное при интерполяции назад
            result.push_back(reverseInterpolation(t, coord, finiteDifferences));
        }
    }

    //Print_result_start//
    cout << endl;

    cout << GREEN;
    cout << "Answer:\n";
    cout << "+--------+--------+--------+--------+--------+\n";
    cout << "|   y1   |   y2   |   y3   |   y4   |   y5   |\n";
    cout << "+--------+--------+--------+--------+--------+\n";
    cout << "|" << setw(8) << setprecision(5) << result[0]
         << "|" << setw(8) << setprecision(5) << result[1]
         << "|" << setw(8) << setprecision(5) << result[2]
         << "|" << setw(8) << setprecision(5) << result[3]
         << "|" << setw(8) << setprecision(5) << result[4] << "|" << endl;
    cout << "+--------+--------+--------+--------+--------+\n";
    cout << RESET;
    //Print_result_send//

    return 0;
}

///////////////////////////////////////////////////////////////

//Вывод табличек для методов Лагранжа
void LagrangianPrint(vector<vector<float>> &coord, vector<float> &argVal, vector<float> &result) {
    //Print_coord_start//
    cout << endl;

    cout << "Set values:\n";

    cout << "+-------+-------+\n"
         << "|   x   |   y   |\n"
         << "+-------+-------+\n";

    for (auto &i : coord) {
        cout << "|" << setw(7) << setprecision(5) << i[0] << "|" << setw(7) << setprecision(5) << i[1] << "|\n";
    }
    cout << "+-------+-------+\n";
    //Print_coord_end//

    //Print_argVal_start//
    cout << endl;

    cout << "The points where we need to find the function value:\n";

    cout << "+";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "--------+";
    }
    cout << endl;

    cout << "|";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "   x" << i << "   |";
    }
    cout << endl;

    cout << "+";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "--------+";
    }
    cout << endl;

    cout << "|";
    for (float i : argVal) {
        cout << setw(8) << setprecision(5) << i << "|";
    }
    cout << endl;

    cout << "+";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "--------+";
    }
    cout << endl;
    //Print_argVal_end//

    //Print_result_start//
    cout << endl;

    cout << GREEN;
    cout << "Answer:\n";

    cout << "+";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "--------+";
    }
    cout << endl;

    cout << "|";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "   y" << i << "   |";
    }
    cout << endl;

    cout << "+";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "--------+";
    }
    cout << endl;

    cout << "|";
    for (int i = 0; i < argVal.size(); i++) {
        cout << setw(8) << setprecision(5) << result[i] << "|";
    }
    cout << endl;

    cout << "+";
    for (int i = 0; i < argVal.size(); i++) {
        cout << "--------+";
    }
    cout << endl;
    cout << RESET;
    //Print_result_send//
}

///////////////////////////////////////////////////////////////

/*
#########################
##-Lagrangian Unqually-##
#########################
*/

//Метод Лагранжа для неравотстоящихно узлов
void Lagrangian_Unequally() {
    cout << CYAN << "+-----Lagrangian Unequally-----+\n" << RESET;

    vector<float> result;

    for (int k = 0; k < argValLagUneq.size(); k++) {
        float stepRes = 0.0;

        for (int i = 0; i < coordLagUneq.size(); i++) {
            float temp = 1.0;

            for (int j = 0; j < coordLagUneq.size(); j++) {
                if (i != j) {
                    //Вычисление членов произведения
                    temp *= (argValLagUneq[k] - coordLagUneq[j][0]) / (coordLagUneq[i][0] - coordLagUneq[j][0]);
                }
            }

            //Полученное произвдевение умножаем на Yi
            stepRes += temp * coordLagUneq[i][1];
        }
        result.push_back(stepRes);
    }

    LagrangianPrint(coordLagUneq, argValLagUneq, result);
}

///////////////////////////////////////////////////////////////

/*
########################
##-Lagrangian Equally-##
########################
*/

//Метод Легранжа для равотстоящихно узлов
void Lagrangian_Equally() {
    cout << BLUE << "+-----Lagrangian Equally-----+\n" << RESET;

    vector<float> result;

    float step = coord[1][0] - coord[0][0];

    for (float k : argVal) {
        float stepRes = 0.0;

        for (int i = 0; i < coord.size(); i++) {
            float temp = 1.0;

            for (int j = 0; j < coord.size(); j++) {
                if (i != j) {
                    //Вычисление членов произведения
                    temp *= (k - coord[0][0] - j * step) / (step * (i - j));
                }
            }

            //Полученное произвдевение умножаем на Yi
            stepRes += temp * coord[i][1];
        }
        result.push_back(stepRes);
    }

    LagrangianPrint(coord, argVal, result);
}

///////////////////////////////////////////////////////////////

//Главная функция кода
int main() {
    logotype();

    Lagrangian_Unequally();
    Lagrangian_Equally();
    Newton();

    return 0;
}


