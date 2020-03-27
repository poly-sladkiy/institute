/* **************************************************************** */
/* filename: whitebear.cpp                                          */
/* abstract: the program displays the text of the file line by line */
/* description:                                                     */
/* creation date: 17/02/2020                                        */
/* autor: Ignakov Konstantin                                        */
/* notes/platform/copyringhts: OS Linux, FreeWare                   */
/* **************************************************************** */

#include <iostream>
#include <stdlib.h>
#include <termios.h>

int main(int argc, char const *argv[]){

	if (argc == 1){
		std::cout << "usage: ./app file.txt" << std::endl;
		std::cout << "\t no input file" << std::endl;
		return 0;
	};
	if (argc > 2){
		std::cout << "usage: ./app file.txt" << std::endl;
		std::cout << "\t more then one file" << std::endl;
		return 0;
	};
	if ((argc == 2) && ((!strcmp(argv[1], "--help")) || !strcmp(argv[1], "-h"))){
		std::cout << "usage: ./app file.txt" << std::endl;
		std::cout << "\tINFO: the program displays the text of the file line by line" << std::endl;
		std::cout << "\t-[h]elp\tshow this text" << std::endl;
		return 0;
	};

	FILE* fp;
	char ch;
	if((fp=fopen(argv[1], "r")) == NULL) {
		std::cout << "\x1B[31mFile: \x1B[0m"<< argv[1] <<"\n\x1B[31mDoes not exsist!\x1B[0m\n";
		return 0;
	}
	else{

		struct termios savetty;
		struct termios tty;

		tcgetattr (0, &tty);
		savetty = tty; // Сохранить упр. информацию канонического режима

		tty.c_lflag &= ~(ICANON|ECHO|ISIG);
		tty.c_cc[VMIN] = 1;
		tcsetattr (0, TCSAFLUSH, &tty);
 
		std::cout << "--------BEGIN OF FILE--------\n";
		while((ch=getc (fp)) != EOF){
			while(ch != '\n'){
				std::cout << ch;
				ch = getc(fp);
			}
			while(getchar() != '\n');
			std::cout << std::endl;
		}
		fclose (fp);
		std::cout << "---------END OF FILE---------\n";
		tcsetattr (0, TCSAFLUSH, &savetty);
	}
	return 0;
}
