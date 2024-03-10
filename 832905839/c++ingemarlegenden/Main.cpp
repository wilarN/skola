#include <iostream>
#include <Windows.h>
#include <cstdlib>
#include <ctime>
#include <string>


int getRandomNumber() {
	// Returnerar ett random nummer mellan 1 och 100, baserat på seeden i main tagen från tiden
	return rand() % 100 + 1;
}

void printMessage(std::string msg) {
	// Skriver ut meddelandet
	std::cout << msg << std::endl;
}

int calculateSum(int a, int b) {
	// Returnerar summan av a och b
	return a + b;
}

int main()
{	
	// Seed för att få olika random nummer varje gång --> time(nullptr) i unix-tid
	srand(static_cast<unsigned int>(time(nullptr)));

	// Random number
	std::cout << getRandomNumber() << std::endl;
	// Print message
	printMessage("Hello World!");

	// Calculate sum funktionen
	std:: cout << calculateSum(5, 5) << std::endl;


	// String manipulation
	std::string name = "William";
	std::string message = name + " is learning C++ functions, loops, and more! (perchance)";
	printMessage(message);

	// Integer operations
	int a = getRandomNumber();
	int b = getRandomNumber();
	std::cout << calculateSum(a, b) << std::endl;

	// Loop with function calls
	for (int i = 0; i < 5; i++) {
		int num = getRandomNumber();
		printMessage("Iteration[" + std::to_string(i) + "]: " + std::to_string(num));
	}

	// För att hålla kvar terminalen
	std::cin.get();
}