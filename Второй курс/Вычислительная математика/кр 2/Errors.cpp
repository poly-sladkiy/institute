#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include "FuncAndDeriv.h"

using namespace std;

double a{0}, b{1};
int n1{10};
double h1{(b - a) / n1};

//Векторы для решения в 8 итераций
vector<double> h1_x = {};
vector<double> h1_y = {};
vector<double> h1_x_1_2 = {};
vector<double> h1_y_1_2 = {};


//Вычисление погрешности для метода центральных прямоугольников
double RectangleError(vector<double> &h_x, double h)
{
	double res, max(-1.0), temp;

	for (int i = 0; i < h_x.size(); i++)
	{
		temp = secondDerivative(h_x[i]);

		if (abs(temp) > max)
		{
			max = temp;
		}
	}

	res = ((b - a) / 24) * h * h * max;

	return res;
}

//Вычисление погрешности для метода левых-правых прямоугольников

double LeftAndRightsRectangleError(vector<double> &h_x, double h)
{
	double res, max(-1.0), temp;

	for (int i = 0; i < h_x.size(); i++)
	{
		temp = firstDerivative(h_x[i]);

		if (abs(temp) > max)
		{
			max = temp;
		}
	}

	res = (b - a) / 2 * h * max;

	return res;
}

//Вычисление погрешности для метода Симпсона
double SimpsonError(vector<double> &h_x, double h)
{
	double res, max(-1.0), temp;

	for (int i = 0; i < h_x.size(); i++)
	{
		temp = thirdDerivative(h_x[i]);

		if (abs(temp) > max)
		{
			max = temp;
		}
	}

	res = ((b - a) / 288) * h * h * h * max;

	return abs(res);
}

//Вычисление погрешности для метода трапеций
double TrapezoidError(vector<double> &h_x, double h)
{
	double res, max(-1.0), temp;

	for (int i = 0; i < h_x.size(); i++)
	{
		temp = secondDerivative(h_x[i]);

		if (abs(temp) > max)
		{
			max = temp;
		}
	}

	res = ((b - a) / 12) * h * h * max;

	return res;
}

//Функция для получения решения и вывода таблиц
void GetSolution()
{
	double temp1{a};
	int i1{0};

	cout << "+-----+----------+----------+----------+----------+" << endl;
	cout << "|  i  |   x(i)   |   y(i)   | x(i)-0.5 | y(i)-0.5 |" << endl;
	cout << "+-----+----------+----------+----------+----------+" << endl;
	do
	{
		h1_x.push_back(temp1);
		h1_y.push_back(func(temp1));
		temp1 += h1;
		if (i1 == 0)
		{
			h1_x_1_2.push_back(0.0);
			h1_y_1_2.push_back(0.0);
		}
		else
		{
			h1_x_1_2.push_back((h1_x[i1 - 1] + h1_x[i1]) / 2);
			h1_y_1_2.push_back(func(h1_x_1_2[i1]));
		}
		cout << "| " << setw(3) << i1 << " | " << setw(8) << h1_x[i1] << " | " << setw(8) << h1_y[i1] << " | " << setw(8) << h1_x_1_2[i1] << " | " << setw(8) << h1_y_1_2[i1] << " | " << endl;
		i1++;
	} while (temp1 <= b);
	cout << "+-----+----------+----------+----------+----------+" << endl
		 << endl;
}


int main()
{
	//Вызов функции получения решения
	GetSolution();

	
	cout << fixed << setprecision(15)
		<< "Rectangle error: " << RectangleError(h1_x, h1) << '\n' << '\n'
		<< "Simpson error: " << SimpsonError(h1_x, h1) << '\n' << '\n'
		<< "Trapezoid error: " << TrapezoidError(h1_x, h1) << '\n' << '\n'
		<< "Left and Right Rectangle error: " << LeftAndRightsRectangleError(h1_x, h1) << '\n' << '\n';

	return 0;
}