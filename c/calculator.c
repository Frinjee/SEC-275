#include <stdio.h>

int main() {

	char operator;
	double num1, num2, result;

	printf("\nEnter an operator (+ - * /): ");
	scanf("%c", &operator);

	printf("\nEnter first number: ");
	scanf("%lf", &num1);
	printf("\nEnter Second number: ");
	scanf("%lf", &num2);

	switch(operator){

		case '+':
			result = num1 + num2;
			printf("\nAddition Result: %.2lf", result);
			break;

		case '-':
			result = num1 - num2;
			printf("\nSubtration Result: %.2lf", result);
			break;

		case '*':
			result = num1 * num2;
			printf("\nMultiplication Result: %.2lf", result);
			break;

		case '/':
			result = num1 / num2;
			printf("\nDivision Result: %.2lf", result);
			break;

		default:
			printf("\n%c is not valid", operator);
	}
}