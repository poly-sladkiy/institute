#include <vector>

#ifndef LR_5_FACTORIAL
#define LR_5_FACTORIAL

int factorial(int n) {
    return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

#endif

#ifndef LR_5_LAGRANGIAN_SOLUTION_H
#define LR_5_LAGRANGIAN_SOLUTION_H

using v = std::vector<double>;
using vv = std::vector<std::vector<double>>;

namespace lagrangian{
    vv atFirstDerivative(const vv &coordinates)
    {
        //Вычисление шага h
        const double h = coordinates[1][0] - coordinates[0][0];
        vv res = vv(12, v(2));

        //Вычисление yi yi+1 yi+2 yi+3 yi+4 по формулам лагранжа при n = 4
        for (int i = 0; i < 12; i += 3)
        {
            res[i][0]     = coordinates[i][0];
            res[i + 1][0] = coordinates[i + 1][0];
            res[i + 2][0] = coordinates[i + 2][0];

            res[i][1]     = (-3 * coordinates[i][1] + 4 * coordinates[i + 1][1] - coordinates[i + 2][1]) / 2 / h;
            res[i + 1][1] = (-coordinates[i][1] + coordinates[i + 2][1]) / 2 / h;
            res[i + 2][1] = (coordinates[i][1] -4 * coordinates[i + 1][1] + 3 * coordinates[i + 2][1]) / 2 / h;

        }
        return res;
    }

    vv atSecondDerivative(const vv &coordinates)
    {
        //Вычисление шага h
        double h       = coordinates[1][0] - coordinates[0][0];
        vv res = vv(12, v(2));

        //Нахождение вторых произовдных yi yi+1 yi+2 yi+3
        //при помощи формул производых высшего порядка
        for (int i = 0; i < 12; i += 4)
        {
            res[i][0]     = coordinates[i][0];
            res[i + 1][0] = coordinates[i + 1][0];
            res[i + 2][0] = coordinates[i + 2][0];
            res[i + 3][0] = coordinates[i + 3][0];

            res[i][1]     = ((2.0 * coordinates[i][1] - 5.0 * coordinates[i + 1][1] + 4.0 * coordinates[i + 2][1] - coordinates[i + 3][1]) / (h*h));
            res[i + 1][1] = ((coordinates[i][1] - 2.0 * coordinates[i + 1][1] + coordinates[i + 2][1]) / (h*h));
            res[i + 2][1] = ((coordinates[i + 1][1] - 2.0 * coordinates[i + 2][1] + coordinates[i + 3][1]) / (h*h));
            res[i + 3][1] = ((-(coordinates[i][1]) + 4.0 * coordinates[i + 1][1] - 5.0 * coordinates[i + 2][1] + 2.0 * coordinates[i + 3][1]) / (h*h));
        }

        return res;
    }
}


#endif //LR_5_LAGRANGIAN_SOLUTION_H
