// compile with gcc Notes.c -o Notes
// run with ./Notes

// comment
/*
	multi
	line 
	comment
*/

// escape sequence (e.g. \n, \t)
// variables (declaration & initialization)
// data types & format specifies
// constants
/* arithmetic operators
	addition(+), subtractions(-), multiplication(*),
	division(/), modulus(%), increment(++), decrement(--)
*/
// augmented assignment operators (+=, -=, *=, /=)
// user input

#include <stdio.h>
#include <string.h>

int main() {
	// constant
	const float ID = 1999.2133;

	// precede with type
	int x;
	x = 5;
	int y = 101;

	char name[] = "Jen";
	int age = 30; 
	float height = 5.4;
	char gender = 'f';

	int z = x + y; // sub, multiply
	int j = x / y; // will be truncated
	int m = x % y; // modulus, gives remainder of division

	//float k = x / y; ** if dividing by integer, 
	//				      it will truncate decimal portion **
	float l = x / (float) y;

	// j + j + 1
	j += 1;

	// variable for user input
	int houseNumber;
	char favNeighbor[25]; // bytes



	printf("\nHello \tWorld");
	printf("\nThis is a new line");
	printf("\'This is a quote\'");

	// format specifier
	printf("\nHello %s", name);
	printf("\nYou are %d years old", age);
	printf("\nYour height is: %f", height);
	printf("\nYour gender is: %c", gender);
	printf("\nYour ID is: %f", ID);

	// User input
	printf("\nEnter House Number: ");
	scanf("%d", &houseNumber); // (& = addr of operator)
	// houseNumber[strlen(houseNumber)-1] = '\0'; | gets rid of newline char
	printf("\nHouse Number: %d", houseNumber);
	
	
	printf("\nEnter Your Favorite Neighbor: ");
	//scanf("%s", favNeighbor);
	fgets(favNeighbor, 25, stdin);
	printf("\nYour Favorite Neighbor is: %s", favNeighbor);
	

	// Arithemetic Ops
	printf("\nArithemitic Operations: ");
	printf("\nAdditon: %d, Incremented Truncated Division(int): %d", z, j);
	printf("\nFloat Division(Casting): %f, Modulus: %d:\n", l, m);

	return 0;
}