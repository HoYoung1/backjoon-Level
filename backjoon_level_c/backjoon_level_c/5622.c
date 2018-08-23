#include <stdio.h>

int main() {
	char dial[16];

	scanf("%s", dial);
	int sum = 0;
	int i;
	for (i = 0; dial[i] != '\0'; i++) {
		if (dial[i]<='C') {
			sum = sum + 3;
		}
		else if (dial[i] <= 'F') {
			sum = sum + 4;
		}
		else if (dial[i] <= 'I') {
			sum = sum + 5;
		}
		else if (dial[i] <= 'L') {
			sum = sum + 6;
		}
		else if (dial[i] <= 'O') {
			sum = sum + 7;
		}
		else if (dial[i] <= 'S') {
			sum = sum + 8;
		}
		else if (dial[i] <= 'V') {
			sum = sum + 9;
		}
		else if (dial[i] <= 'Z') {
			sum = sum + 10;
		}
	}

	printf("%d", sum);

	return 0;
}