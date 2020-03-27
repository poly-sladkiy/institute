/* **************************************************************** */
/* filename: bad_east.cpp                                          */
/* abstract: The program makes a database or displays it on the     */
/*   	   	 screen. the app is intended for computer classes,      */
/*			 computer stores, and others.                           */
/* description:                                                     */
/* creation date: 2020/03/03                                        */
/* autor: Ignakov Konstantin                                        */
/* notes/platform/copyringhts: OS Linux, FreeWare                   */
/* **************************************************************** */

#include <iostream>
#include <string.h>

void INFO ();
void logotype();
void writeDB (int, char const **);
void readDB (int, char const **);

int main(int argc, char const *argv[]){

	if ((argc == 1) || (argc == 3) || (argc > 4)){
		std::cout << "\x1B[32musage\x1B[0m: ./bad_east [ -r | -c ] N file\n"
			<< "\tN\t\t- number of records\n"
			<< "\t[-h | --help]\t-for more information\n";
		return 0;
	}

	if ((argc == 2) && ((!strcmp(argv[1], "--help")) || !strcmp(argv[1], "-h"))){
		std::cout << "\ncompleted by\n";
		logotype();
		INFO();
	}

	// write data 2 file
	if (!strcmp(argv[1], "-c")){
		writeDB(argc, argv);
		return 0;
	}

	// read DB
	if (!strcmp(argv[1], "-r")){
		readDB(argc, argv);
    	return 0;
	}

	return 0;
}
