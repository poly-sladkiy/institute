/* **************************************************************** */
/* filename: main.cpp                                               */
/* abstract: The program makes a database.                          */
/*			 the app is intended for computer classes,              */
/*			 computer stores, and others.                           */
/* description:                                                     */
/* creation date: 2020/03/04                                        */
/* autor: Ignakov Konstantin                                        */
/* notes/platform/copyringhts: OS Linux, FreeWare, MacOS            */
/* **************************************************************** */

#include <iostream>
#include <fstream>

std::string center(int, const std::string&);
std::string center(int, const int&);
void logotype();
void INFO();

class technicalParameters{
private:
	std::string name_socket;
	int gigahertz;
	int random_access_memory;
	int permanent_memory;
	std::string type_of_monitor;
public:
	std::string get_socket(){return name_socket;};
	int get_gHz(){return gigahertz;};
	int get_ram(){return random_access_memory;};
	int get_rom(){return permanent_memory;};
	std::string get_monitor(){return type_of_monitor;};

	void set(std::string socket, int gHz, int RAM, int ROM, std::string monitor){
		name_socket=socket; gigahertz=gHz; random_access_memory=RAM; permanent_memory=ROM; type_of_monitor=monitor;};
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

int main(int argc, char const *argv[]){

	if ((argc == 1) || (argc == 3) || (argc > 4)){
		std::cout << "\x1B[32musage\x1B[0m: ./snow_man [ -r | -c ] N file\n"
			<< "\tN\t\t- number of records\n"
			<< "\t[-h | --help]\t-for more information\n";
		return 0;
	}

	if ((argc == 2) && ((!strcmp(argv[1], "--help")) || !strcmp(argv[1], "-h"))){
		std::cout << "\ncompleted by\n";
		logotype();
		INFO();
	}

	if((argc==4) && (!strcmp(argv[1],"-c")) && (atoi(argv[2])!=0)){
 		std::ofstream fp(argv[3],std::ios::binary);
 		if(fp.is_open()) {
 			int N=atoi(argv[2]);
 			if(N<=0){std::cout<<"\x1B[31;5mError, n<=0\x1B[0m"<<std::endl;}

 			technicalParameters pc;
 			std::string socket;
 			int gHz;
 			int RAM;
 			int ROM;
 			std::string monitor;

 			fp << N << std::endl;
 			for(int i = 0; i < N; i++){
 				std::cout << "#" << i + 1 << "\nSocket:    ";
				std::cin >> socket;
				std::cout << "Gigahertz: ";
				gHz = enter_AND_check();
				std::cout << "RAM:\t   ";
				RAM = enter_AND_check();
				std::cout << "ROM:\t   ";
				ROM = enter_AND_check();
				std::cout << "Monitor:   ";
				std::cin >> monitor;
	 			pc.set(socket, gHz, RAM, ROM, monitor);

 				fp << pc.get_socket() << " "
 				   << pc.get_gHz() << " "
 				   << pc.get_ram() << " "
 				   << pc.get_rom() << " "
 				   << pc.get_monitor() << std::endl;
 			}
 			fp.close();
 		}
 	}

 	if((argc==4) && (!strcmp(argv[1],"-r")) && (atoi(argv[2])!=0)){
 		std::ifstream fin(argv[3]);

		if (!fin.is_open()){
			std::cout << "\x1B[1;5;31mError:!\n"
				<< "File cannot be open for read!\x1B[0m\n";
			exit(1);
		}
		else{

			std::string msg;
			int N = std::atoi(argv[2]);
			if(N<=0){std::cout<<"\x1B[31;5mError, n<=0\x1B[0m"<<std::endl;}

			std::string socket;
 			int gHz;
 			int RAM;
 			int ROM;
 			std::string monitor;

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
				fin >> socket >> gHz >> RAM >> ROM >> monitor;

				std::cout << "|" << center(13, socket)
					<< "|" << center(9, gHz)
					<< "|" << center(9, RAM)
					<< "|" << center(9, ROM)
					<< "|" << center(11, monitor) << "|\n"
					<< "+-------------+---------+---------+---------+-----------+\n";

			}
		}
 	}

	return 0;
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
