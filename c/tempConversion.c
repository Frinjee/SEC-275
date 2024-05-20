#include <stdio.h>
#include <ctype.h>

int main() {

	char unit;
	float temp;

	printf("\nIs the temp in (F) or (C)?: \n");
	scanf("%c", &unit);

	// unit = toUpper(unit);

	if (unit == 'C' || unit == 'c') {

		printf("\nCelsius to Farenheiht\n");
		printf("\nEnter Temperature: ");
		scanf("%f", &temp);
		temp = (temp * 9 / 5) + 32;
		printf("\nThe Temperature is: %.1f\nc", temp);

	} else if (unit == 'F' || unit == 'f') {

		printf("\nFarenheiht to Celsius\n");
		printf("\nEnter Temperature: ");
		scanf("%f", &temp);
		temp = ((temp - 32) * 5) / 9;
		printf("\nThe Temperature is: %.1f\nc", temp);

	} else {printf("\n%c is not a valid unit of measurement: \n", unit);}
}