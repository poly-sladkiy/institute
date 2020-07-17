#include <iostream>
#include <stdio.h>
#include "my_lib.h"

int my_len(const char*);

template<typename T>
T SecureInputValue();

template<typename T>
bool EqualString(const T, const T);

// Parent-class
class Worker{
private:
	int id = 1;
	std::string name;

public:
	//Worker(){ id = 0; name[0] = '\0';};
	Worker() = default;
	~Worker() = default;
	void set_information(int _id, std::string _name){id = _id; name = _name;};

	void print();
	virtual void work() = 0;
};

// Son-class
class Student : public Worker{
public:
	//Student() : Worker(){};
	Student() = default;
	~Student() = default;

	void work() {std::cout<<" Hello, Dummy\n";}
};

// Son-class
class Programmer : public Worker{
public:
	//Programmer() : Worker() {};
	Programmer() = default;
	~Programmer() = default;

	void work() {std::cout<<" I'm in the system\n";}
};

// Son-class
class Tester : public Worker{
public:
	//Tester() : Worker() {};
	Tester() = default;
	~Tester() = default;

	void work() {std::cout<<" Your program is an error\n";}
};

// Son-class
class Director : public Worker{
public:
	//Director() : Worker() {};
	Director() = default;
	~Director() = default;

	void work() {std::cout<<" The sun is still high in the sky.\n";}
};



int main(int argc, char const *argv[]){

	// for dynamic array
	int N;
	std::cout << "Enter the number of employees: ";
	N = SecureInputValue<int>();
	Worker* mass[N];

	for (int i = 0; i < N; ++i){
		int identification_number;
		std::string name_employee;
		std::string position;

		std::cout << '\n';

		// collecting information about an employee
		std::cout << "Enter identification number of employee #" << i + 1 << " : ";
		identification_number = SecureInputValue<int>();
		std::cout << "Enter name of employee: ";
		std::cin >> name_employee;
		std::cout << "Enter job of employee: ";
		std::cin >> position;

		// looking for a profession
		if("student" == position){ mass[i] = new Student; mass[i]->set_information(identification_number, name_employee); continue;};
		if("programmer" == position){mass[i] = new Programmer; mass[i]->set_information(identification_number, name_employee); continue;};
		if("tester" == position){mass[i] = new Tester; mass[i]->set_information(identification_number, name_employee); continue;};
		if("director" == position){mass[i] = new Director; mass[i]->set_information(identification_number, name_employee); continue;};

		std::cout << "There is no such position in the organization\n"; return 0;
	}

	for(int i = 0; i < N; i++){
		mass[i] -> print();
		mass[i] -> work();
	}
	

	std::cout << '\n';
	return 0;
}

void Worker::print(){
	std::cout << "ID: " << id << ". Name: " << name << ". ";
}
