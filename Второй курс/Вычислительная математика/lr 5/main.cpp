#include <iostream>
#include <iomanip>

#include "poly/logotype.h"

#include "NewtonSolution.h"
#include "LagrangianSolution.h"

int main() {

    std::cout << logotype << std::endl << std::endl;

    const std::vector<std::vector<double>> coord = {
            {1.340, 4.25562},
            {1.345, 4.35325},
            {1.350, 4.45522},
            {1.355, 4.56184},
            {1.360, 4.67344},
            {1.365, 4.79038},
            {1.370, 4.91306},
            {1.375, 5.04192},
            {1.380, 5.17744},
            {1.385, 5.32016},
            {1.390, 5.47069},
            {1.395, 5.62968},
    };

    std::cout << "\t\tNewton" << std::endl << std::endl;

    auto first = newton::atFirstDerivative(coord);
    std::cout << "First derivative" << std::endl;
    for (const auto &i : first) {
        std::cout << left
                  << setprecision(4) << std::setw(7) << i[0]
                  << "\t"
                  << setprecision(5) << setw(5) << i[1]
                  << std::endl;
    }

    std::cout << std::endl;

    auto second = newton::atSecondDerivative(coord);
    std::cout << "Second derivative" << std::endl;
    for (const auto &i : second) {
        std::cout << left
                  << setprecision(4) << std::setw(7) << i[0]
                  << "\t"
                  << setprecision(5) << setw(5) << i[1]
                  << std::endl;
    }

    std::cout << std::endl;

    std::cout << "\t\tLagrangian" << std::endl << std::endl;

    first = lagrangian::atFirstDerivative(coord);
    std::cout << "First derivative" << std::endl;
    for (const auto &i : first) {
        std::cout << left
                  << setprecision(4) << std::setw(7) << i[0]
                  << "\t"
                  << setprecision(5) << setw(5) << i[1]
                  << std::endl;
    }

    std::cout << std::endl;

    second = lagrangian::atSecondDerivative(coord);
    std::cout << "Second derivative" << std::endl;
    for (const auto &i : second) {
        std::cout << left
                  << setprecision(4) << std::setw(7) << i[0]
                  << "\t"
                  << setprecision(5) << setw(5) << i[1];
        std::cout << endl;
    }

    return 0;
}
