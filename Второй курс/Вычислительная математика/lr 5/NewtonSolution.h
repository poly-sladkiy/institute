#include <vector>

using namespace std;

#ifndef LR_5_FACTORIAL
#define LR_5_FACTORIAL

int factorial(int n) {
    return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

#endif


#ifndef LR_5_NEWTON_SOLUTION_H
#define LR_5_NEWTON_SOLUTION_H

using v = std::vector<double>;
using vv = std::vector<std::vector<double>>;

namespace newton{
/// Функция для нахождения конечных разностей
vv atFiniteDifferences(const vv &coordinates) {
    vv finiteDifferences{};

    v tempList{};
    for (int i = 0; i < coordinates.size() - 1; i++) {
        //Вычисление конечных разностей
        tempList.push_back(coordinates[i + 1][1] - coordinates[i][1]);
    }

    finiteDifferences.push_back(tempList);

    for (int i = 0; i < coordinates.size() - 2; i++) {
        tempList = {};    //инициализация промежуточного списка пустым списком
        for (int j = 0; j < finiteDifferences.at(i).size() - 1; j++) {
            //Вычисление конечных разностей
            tempList.push_back(finiteDifferences.at(i).at(j + 1) - finiteDifferences.at(i).at(j));
        }
        finiteDifferences.push_back(tempList);
    }

    return finiteDifferences;
}

/// Я тоже не ебу зачем ещё цикл, влад почему-то считает
/// всё по шагам, сначала первая часть, потом середина
/// и конец

/// Вторая производная
vv atFirstDerivative(const vv &coordinates) {

    /// Измените тут значения под ваш массив данных

    //Вычисление шага
    double h = coordinates[1][0] - coordinates[0][0];
    vv resArr(12, v(2));

    //Нахождение производных для первых 6ти членов
    //выделяем координаты необходимых точек
    vv tempArr(12, v(2));
    for (int i = 0; i < 12; i++) {
        tempArr[i][0] = coordinates[i][0];
        tempArr[i][1] = coordinates[i][1];
    }

    vv finiteDifference = atFiniteDifferences(tempArr);

    //Расчет производных по формуле
    for (int i = 0; i < 12; i++) {
        double t = (coordinates[i][0] - coordinates[0][0]) / h;

        resArr[i][0] = coordinates[i][0];
        resArr[i][1] = (finiteDifference.at(0).at(0)
                        + ((2.0 * t - 1) * finiteDifference.at(1).at(0) / factorial(2))
                        + ((3.0 * t * t - 6.0 * t + 2) * finiteDifference.at(2).at(0) / factorial(3)
                           + ((4.0 * t * t * t + 18.0 * t * t + 22.0 * t - 6.0) * finiteDifference.at(3).at(0)) /
                             factorial(4))
                        + ((5.0 * t * t * t * t - 40.0 * t * t * t + 105.0 * t * t - 100.0 * t + 24.0) *
                           finiteDifference.at(4).at(0) / factorial(5)))
                       / h;
    }

    /// У Влада ещё 2 цикла, у меня числа в целом норм и с одним

    //Нахождение производных для следующих 3 членов
    //выделяем координаты необходимых точек
    tempArr = vv(6, v(2));
    for (int i = 6, j = 0; i < 12; i++, j++) {
        tempArr[j][0] = coordinates[i][0];
        tempArr[j][1] = coordinates[i][1];
    }
    //Получаем список конечных приращений
    finiteDifference = atFiniteDifferences(tempArr);

    //Расчет производных по формуле
    for (int i = 6; i < 12; i++) {
        double t = (coordinates[i][0] - coordinates[6][0]) / h;

        resArr[i][0] = coordinates[i][0];
        resArr[i][1] = (finiteDifference.at(0).at(0)
                        + ((2.0 * t - 1) * finiteDifference.at(1).at(0) / factorial(2))
                        + ((3.0 * t * t - 6.0 * t + 2) * finiteDifference.at(2).at(0) / factorial(3)
                           + ((4.0 * t * t * t + 18.0 * t * t + 22.0 * t - 6.0) * finiteDifference.at(3).at(0)) /
                             factorial(4))
                        + ((5.0 * t * t * t * t - 40.0 * t * t * t + 105.0 * t * t - 100.0 * t + 24.0) *
                           finiteDifference.at(4).at(0) / factorial(5)))
                       / h;
    }

    /// Я хуй знает что это, но если это запустить значения производной у меня будут ебейшие

//    //Нахождение производных для последних 6ти членов
//    //выделяем координаты необходимых точек
//    tempArr = vv(6, v(2));
//    for (int i = 9, j = 0; i < 12; i++, j++) {
//        tempArr[j][0] = coordinates[i][0];
//        tempArr[j][1] = coordinates[i][1];
//    }
//    //Получаем список конечных приращений
//    finiteDifference = atFiniteDifferences(tempArr);
//
//
//    //Расчет производных по формуле
//    for (int i = 9; i < 12; i++) {
//        double t = (coordinates[i][0] - coordinates[9][0]) / h;
//
//        resArr[i][0] = coordinates[i][0];
//        resArr[i][1] = (finiteDifference.at(0).at(0)
//                        + ((2.0 * t - 1) * finiteDifference.at(1).at(0) / factorial(2))
//                        + ((3.0 * t * t - 6.0 * t + 2) * finiteDifference.at(2).at(0) / factorial(3)
//                           + ((4.0 * t * t * t + 18.0 * t * t + 22.0 * t - 6.0) * finiteDifference.at(3).at(0)) /
//                             factorial(4))
//                        + ((5.0 * t * t * t * t - 40.0 * t * t * t + 105.0 * t * t - 100.0 * t + 24.0) *
//                           finiteDifference.at(4).at(0) / factorial(5)))
//                       / h;
//    }

    return resArr;

}

vv atSecondDerivative(const vv &coordinates) {

    /// Измените тут значения под ваш массив данных

    //Вычисление шага
    double h = coordinates[1][0] - coordinates[0][0];
    vv resArr(12, v(2));

    //Нахождение производных для первых 6ти членов
    //выделяем координаты необходимых точек
    vv tempArr(12, v(2));
    for (int i = 0; i < 12; i++) {
        tempArr[i][0] = coordinates[i][0];
        tempArr[i][1] = coordinates[i][1];
    }
    //Получаем список конечных приращений
    vv finiteDifference = atFiniteDifferences(tempArr);

    //Расчет производных по формуле
    for (int i = 0; i < 12; i++) {
        double t = (coordinates[i][0] - coordinates[0][0]) / h;

        resArr[i][0] = coordinates[i][0];
        resArr[i][1] = (finiteDifference.at(1).at(0)
                        + ((6.0 * t - 6.0) * finiteDifference.at(2).at(0) / factorial(3))
                        + ((12.0 * t * t - 36.0 * t + 22.0) * finiteDifference.at(3).at(0) / factorial(4)
                           + ((20.0 * t * t * t - 120.0 * t * t + 210.0 * t - 100.0) * finiteDifference.at(4).at(0)) /
                             factorial(5)))
                       / (h * h);
    }

    /// Я тоже не ебу зачем ещё цикл, влад почему-то считает
    /// всё по шагам, сначала первая часть, потом середина
    /// и конец

//    //Нахождение производных для следующих 3 членов
//    //выделяем координаты необходимых точек
//    tempArr = vv(6, v(2));
//    for (int i = 6, j = 0; i < 12; i++, j++)
//    {
//        tempArr[j][0] = coordinates[i][0];
//        tempArr[j][1] = coordinates[i][1];
//    }
//    //Получаем список конечных приращений
//    finiteDifference = atFiniteDifferences(tempArr);
//
//    //Расчет производных по формуле
//    for (int i = 6; i < 12; i++)
//    {
//        double t = (coordinates[i][0] - coordinates[6][0]) / h;
//
//        resArr[i][0] = coordinates[i][0];
//        resArr[i][1] = (finiteDifference.at(1).at(0)
//                        + ((6.0 * t - 6.0) * finiteDifference.at(2).at(0) / factorial(3))
//                        + ((12.0*t*t - 36.0*t + 22.0) * finiteDifference.at(3).at(0) / factorial(4)
//                           + ((20.0*t*t*t - 120.0*t*t + 210.0*t - 100.0) * finiteDifference.at(4).at(0)) / factorial(5)))
//                       / (h*h);
//    }

    return resArr;
}

}
#endif //LR_5_NEWTON_SOLUTION_H
