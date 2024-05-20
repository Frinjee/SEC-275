// Ternary operator = shorcute to if/else
// (condition) ? value if true: value if false
// Function Prototype
// Function delcaration w/o a body and before main()
// Ensures that calls are made with the correct arguments

#include <stdio.h>
#include <string.h>
#include <ctype.h>

void helloFriend(char[], int); // Function prototype

void birthday(char name[], int age) {

	printf("\nHappy Birthday dear %s\n", name);
	printf("\nYou are %d years old!!\n", age);

}

double square(double sqAge) {

	return sqAge * sqAge;

}

int findMax(int x, double y) {
	
	/*
	if (x > y) {
		return x;
	} else {
		return y;
	}
	*/

	return (x > y) ? x : y;
}


int main() {


	char name[] = "Jen";
	int age = 30;
	double sqAge = square(age);

	int max = findMax(age, sqAge);

	char friendName[] = "Tai";
	int friendAge = 45;

	char firstName[] = "Jen";
	char lastName[] = "Hammond";

	char stringOne[] = "This is a test for copy";
	char stringTwo[] = "Copy Me!";

	//Not usable with gcc on linux
	//strlwr(firstName); // lowercase
	//strupr(firstName); uppercase
	//strcat(firstName, lastName); appends stringTwo > end of stringOne
	//strcat(firstName, lastName, 1); appends n chars from stringTwo > stringOne
	//strcpy(stringOne, stringTwo); copy stringTwo > stringOne
	//strncpy(stringOne, stringTwo); copy n chars of stringTwo > stringOne
	//strset(stringOne, '?');  set all chars of a string to given char
	//strnset(stringOne, 'x', 1); sets first n chars of a string to given char

	int stringResult = strlen(firstName);

	birthday(name, age);
	printf("\nYour Name is %d: in length", stringResult);
	printf("\nYour age squared is: %.1lf", sqAge);
	printf("\nMax between age and squared age: %d\n", max);

	helloFriend(friendName, friendAge);
	
	return 0;
}

void helloFriend(char friendName[], int friendAge) {

	printf("\nHello %s", friendName);
	printf("\nYou are %d years old\n", friendAge);

}
