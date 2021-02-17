#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>

struct technicalParameters{
	char name_socket[20];
	int gigahertz;
	int random_access_memory;
	int permanent_memory;
	char type_of_monitor[20];
};

int enter_AND_check(){
	int a;
	// check enter begin
	while (!(std::cin >> a) || (std::cin.peek() != '\n'))
    {
		std::cin.clear();
		while (std::cin.get() != '\n');
		std::cout << "\x1B[31mError\x1B[0m, retype: " << std::endl;
    }
    //check enter end
    return a;
}

// std has left and rigth, but does noy exsist center:
std::string center(int width, const std::string& str) {
    int len = str.length();
    if(width < len) { return str; }

    int diff = width - len;
    int pad1 = diff/2;
    int pad2 = diff - pad1;
    return std::string(pad1, ' ') + str + std::string(pad2, ' ');
}

std::string center(int width, const int& msg) {
    std::string str = std::to_string(msg);
    int len = str.length();
    if(width < len) { return str; }

    int diff = width - len;
    int pad1 = diff/2;
    int pad2 = diff - pad1;
    return std::string(pad1, ' ') + str + std::string(pad2, ' ');
}

// help
void INFO(){
	std::cout << "usage: ./bad_east [ -r | -c ] N file.txt" << std::endl
		<< "\x1B[32mINFO\x1B[0m: "
		<< "\tThe program builds databases or displays it on the screen.\n"
		<< "\tThe app is intended for computer classes,\n"
		<< "\tcomputer stores, and others.\n\n"
		<< "\x1B[31mparams\x1B[0m:\n"
		<< "\t N\tnumber of entries\n"
		<< "\t-r\tread DataBase from file\n"
		<< "\t-c\twrite DataBase to file\n"
		<< "\t-{-h}elp\tdisplay this text" << std::endl;
	
	exit(1);
}

// if argv[1] == "-c"
void writeDB(int argc, char const *argv[]){

	// check open file for write
	FILE* fp;
	if((fp=fopen(argv[3], "w")) == NULL) {
		std::cout << "\x1B[31mFile: \x1B[0m"<< argv[3] <<"\n\x1B[31mDoes not exsist!\x1B[0m\n";
		exit(1);
	}

	// for enter the data into file
	// ex.: ./bad_east -c 10 PCshop.txt
	if ((argc == 4) && (std::atoi(argv[2]) != 0)){
		int N = std::atoi(argv[2]);
		technicalParameters info;
		std::cout << "\n";

		fprintf(fp, "%d\n", N);
		for (int i = 0; i < N; ++i){
			std::cout << "#" << i + 1 << "\nSocket:    ";
			std::cin >> info.name_socket;
			std::cout << "Gigahertz: ";
			info.gigahertz = enter_AND_check();
			std::cout << "RAM:\t   ";
			info.random_access_memory = enter_AND_check();
			std::cout << "ROM:\t   ";
			info.permanent_memory = enter_AND_check();
			std::cout << "Monitor:   ";
			std::cin >> info.type_of_monitor;

			// write 2 file
			fprintf(fp, "%s %d %d %d %s\n", info.name_socket, info.gigahertz, info.random_access_memory, info.permanent_memory, info.type_of_monitor);

			std::cout << "\n\x1B[32mWell done !! =)\x1B[0m\n";

		}

		fclose(fp);
	}

	return;
}

// if argv[1] == "-r"
void readDB(int argc, char const *argv[]){

		std::ifstream fin(argv[3]);

		if (!fin.is_open()){
			std::cout << "\x1B[1;5;31mError 404!\n"
				<< "File cannot be open!\x1B[0m\n";
			exit(1);
		}
		else{

			std::string msg;
			int N = std::atoi(argv[2]);

			fin >> msg;
			if (N > std::stoi(msg)){
				std::cout << "\x1B[31mYou enter more value, than DB consist!\n\x1B[0m";
				N = std::stoi(msg);
			}

			std::cout << "+-------------+---------+---------+---------+-----------+\n"
				<< "|    \x1B[36msoket\x1B[0m    |   \x1B[36mMHz\x1B[0m   |   \x1B[36mRAM\x1B[0m   |   \x1B[36mROM\x1B[0m   |  \x1B[36mMonitor\x1B[0m  |\n"
				<< "+-------------+---------+---------+---------+-----------+\n";

			for (int i = 0; (i < N) && (!fin.eof()); ++i)
			{
				technicalParameters info;
				fin >> info.name_socket >> info.gigahertz >> info.random_access_memory >> info.permanent_memory >> info.type_of_monitor;

				std::cout << "|" << center(13, info.name_socket)
					<< "|" << center(9, info.gigahertz)
					<< "|" << center(9, info.random_access_memory)
					<< "|" << center(9, info.permanent_memory)
					<< "|" << center(11, info.type_of_monitor) << "|\n"
					<< "+-------------+---------+---------+---------+-----------+\n";

			}
		}

	return;
}
