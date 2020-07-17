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

// help
void INFO(){
	std::cout << "usage: ./snow_man [ -r | -c ] N file.txt" << std::endl
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
