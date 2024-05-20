// compile with gcc NotesTwo.c -o Notes
// run with ./NotesTwo

// Math Functions
// Hypotenuse Calculator
// If functions and Switch Statements

#include <stdio.h>
#include <math.h>

int main() {

	double A, B;
	int C, D, E;
	double F, G, H, I, J;
	double sideA, sideB, sideC;

	int age;
	char type;

	A = sqrt(64);
	B = pow(2, 4);

	C = round(3.14);
	D = ceil(3.14);
	E = floor(3.99);

	F = fabs(-100);
	G = log(3);
	H = sin(45);
	I = cos(45);
	J = tan(45);


	// USER INPUT
	printf("\n****** USER INPUT SECTION ******");
	printf("\nEnter Side A: ");
	scanf("%lf", &sideA);
	printf("\nEnter Side B: ");
	scanf("%lf", &sideB);

	sideC = sqrt(sideA*sideA + sideB*sideB);


	printf("\nEnter your age: ");
	scanf("%d", &age);
	printf("\nEnter your type: ");
	scanf(" %c", &type);

	if(age >= 21) {
		printf("\nYou are old enough\n");	
	} else if (age <= 0) {
		printf("\nInvalid Age: \n");
	} else {
		printf("\nYou are not old enough\n");
	}

	switch(type) {

		case 'A':
			printf("\nYou are type A\n");
			break;
		case 'B':
			printf("\nYou are type B\n");
			break;
		default:
			printf("\nNot a valid type\n");
			break;
	}



	// PRINTING
	printf("\n****** GENERAL MATH SECTION ******");
	printf("\nSquare Root: %lf\n", A);
	printf("\nPower:  %lf\n", B);
	printf("\nRounded:  %d\n", C);
	printf("\nCeiling: %d\n", D);
	printf("\nFloor: %d\n", E);
	printf("\nAbsolute: %lf\n", F);
	printf("\nLog: %lf\n", G);
	printf("\nSin: %lf\n", H);
	printf("\nCos: %lf\n", I);
	printf("\nTan: %lf\n", J);
	printf("\nSide C: %lf\n", sideC);

	return 0;

}