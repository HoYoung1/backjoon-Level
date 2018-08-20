//내실력으로못품 ㅈㅈ

#include <stdio.h>

int main() {
	char *star[3];
	star[0] = "  *  ";
	star[1] = " * * ";
	star[2] = "*****";

	int input; // 3*2^k
	scanf("%d", &input);

	

	if (input == 3) {
		printf("%s\n", star[0]);
		printf("%s\n", star[1]);
		printf("%s\n", star[2]);
	}
	else if (input == 6) {
		printf("   %s\n", star[0]);
		printf("   %s\n", star[1]);
		printf("   %s\n", star[2]);

		printf("%s %s\n", star[0], star[0]);
		printf("%s %s\n", star[1], star[1]);
		printf("%s %s\n", star[2], star[2]);
	}
	else if (input == 12) {
		printf("   %s\n", star[0]);
		printf("   %s\n", star[1]);
		printf("   %s\n", star[2]);

		printf("%s %s\n", star[0], star[0]);
		printf("%s %s\n", star[1], star[1]);
		printf("%s %s\n", star[2], star[2]);

	}

	return 0;
}