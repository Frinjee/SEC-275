#include <stdio.h>
#include <string.h>

int main() {

	char name[25];

	printf("\nEnter your name: ");
	fgets(name, 25, stdin);
	name[strlen(name) - 1] = '\0';

	while(strlen(name) == 0) {
		printf("\nYou did not enter your name: ");
		printf("\nEnter your name: ");
		
		fgets(name, 25, stdin);
		name[strlen(name) - 1] = '\0';
	}

	printf("Incrementing: \n");
	for(int i = 1; i <= 10; i+=2) {
		printf("%d\n", i);
	}

	printf("\nDecrementing: \n");
	for(int i = 10; i >= 1; i-=2) {
		printf("%d\n", i);
	}

	printf("\nHello: %s", name);
	return 0;
}