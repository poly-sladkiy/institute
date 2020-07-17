#ifndef my_lib_h
#define my_lib_h

#include <iostream>

void logotype(){
	char logo[]="\x1B[31m                      (                             \n"             
	"             (        )\\ )  (         (        )           \n"
	"             )\\ (    (()/(  )\\    )   )\\ )  ( /( (   (     \n"
	" `  )    (  ((_))\\ )  /(_))((_)( /(  (()/(  )\\()))\\  )\\ )  \n"
	" /(/(    )\\  _ (()/( (_))   _  )(_))  ((_))((_)\\((_)(()/(  \n" 
	"((_)_\\  ((_)| | )(_))/ __| | |((_)_   _| | | |(_)(_) )(_)) \n"
	"| '_ \\)/ _ \\| || || |\\__ \\ | |/ _` |/ _` | | / / | || || | \n"
	"| .__/ \\___/|_| \\_, ||___/ |_|\\__,_|\\__,_| |_\\_\\ |_| \\_, | \n"
	"|_|             |__/                                 |__/  \n\x1B[0m";

	std::cout << logo << std::endl;
}

// todo: change INFO
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

int my_len(const char* str){
	int i = 0;
	while(str[i++] != '\0');
	return i;
}

// check enter value
template<typename T>
T SecureInputValue(){
	T a;
	while (!(std::cin >> a) || (std::cin.peek() != '\n'))
    {
		std::cin.clear();
		while (std::cin.get() != '\n');
		std::cout << "\x1B[31mError\x1B[0m, enter again: " << std::endl;
    }
    return a;
}

template<typename T>
bool EqualString(const T* str1, const T* str2){
	bool equal = true;
	int len = my_len(str1);

	if(len != my_len(str2)){
		equal = false;
		return equal;
	}

	for(int i = 0; i < len; i++){
		if(str1[i] != str2[i]){
			equal = false;
			break;
		}
	}
	return equal;
}

#endif