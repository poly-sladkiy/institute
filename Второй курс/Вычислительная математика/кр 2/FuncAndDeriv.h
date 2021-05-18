#ifndef _FuncAndDeriv_
#define _FuncAndDeriv_

#include <iostream>
#include <cmath>
using namespace std;


//Функция из задания
double func(double x)
{
	// return log(x + 1) / x * exp(-x);
	return cos(x)*exp(-x)/(x*x + 1);
}

//Первая производная функции
double firstDerivative(double x)
{
	// return (x + x * log(x + 1) * (-x - 1) + (-x - 1) * log(x + 1) / (x * x * x * exp(x) + x * x * exp(x)));
	return (-cos(x)*exp(-x) - exp(-x)*sin(x))/(x*x + 1) - 2*x*cos(x)*exp(-x)/(x*x + 1)/(x*x + 1)/(x*x + 1);
}

//Вторая производная функции
double secondDerivative(double x)
{
	// return (-1/(1 + x)/(1 + x) - 2/(1 + x) + 2*(-1/(1 + x) + log(1 + x))/x + 2*log(1 + x)/x/x + log(1 + x))*exp(-x)/x;
	return 2*((-1 + 4*x*x/(1 + x*x))*cos(x)/(1 + x*x) + 2*x*(cos(x) + sin(x))/(1 + x*x) + sin(x))*exp(-x)/(1 + x*x);
}

//Третья производная функции
double thirdDerivative(double x)
{
	// return (-log(1 + x) + 2/(1 + x)/(1 + x)/(1 + x) + 3/(1 + x) + 3/(1 + x)/(1 + x) - 6*log(1 + x)/x/x/x - 6*(-1/(1 + x) + log(1 + x))/x/x + 3*(pow(1 + x, -2) - log(1 + x) + 2/(1 + x))/x)*exp(-x)/x;
	return -2*(-cos(x) + 3*(-1 + 4*x*x/(1 + x*x))*(cos(x) + sin(x))/(1 + x*x) + 6*x*sin(x)/(1 + x*x) + 12*x*(-1 + 2*x*x/(1 + x*x))*cos(x)/(1 + x*x)/(1 + x*x) + sin(x))*exp(-x)/(1 + x*x);
}



/*
//Функция из задания
double func(double x)
{
	return ((x * x + 1) / (sqrt(x * x + 4)));
	//return exp(-x)/(1 + exp(-x));
}

//Первая производная функции
double firstDerivative(double x)
{
	return (-(x*(x*x+1)/(pow((x*x+4)), (3/2)))+((2*x)/(sqrt(x*x+4))));
	//return exp(-2*x)/pow((1 + exp(-x)), 2) - exp(-x)/(1 + exp(-x));
}

//Вторая производная функции
double secondDerivative(double x)
{
	return ((-(4*x*x)/(x*x+4))+(((x*x+1)*((3*x*x)/(x*x+4)-1))/(x*x+4))+2)/(sqrt(x*x+4));
	//return (1 - 2*exp(-x)/(1 + exp(-x)) - (1 - 2*exp(-x)/(1 + exp(-x)))*exp(-x)/(1 + exp(-x)))*exp(-x)/(1 + exp(-x));
}

//Третья производная функции
double thirdDerivative(double x)
{
	return 3*x*(-4 + 6*x*x/(4 + x*x) - (1 + x*x)*(-3 + 5*x*x/(4 + x*x))/(4 + x*x))/(pow((4 + x*x),(3/2)));
	//return (1 - 2*exp(-x)/(1 + exp(-x)) - (1 - 2*exp(-x)/(1 + exp(-x)))*exp(-x)/(1 + exp(-x)))*exp(-x)/(1 + exp(-x));
}
*/

#endif
