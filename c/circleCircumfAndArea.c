// compile with gcc circleCircumference.c -o circleCircumference
// run with ./circleCircumference

#include <stdio.h>

int main() {

	const double PI = 3.14159;
	double radius, circumference, area;

	printf("\nEnter radius of your circle: ");
	scanf("%lf", &radius);

	circumference = 2 * PI * radius;
	area = PI * radius * radius;

	printf("\nCircumference is: %lf", circumference);
	printf("\nArea is: %lf\n", area);


	return 0;
}