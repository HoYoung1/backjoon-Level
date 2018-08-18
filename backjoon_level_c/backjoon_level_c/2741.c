#include <stdio.h>

int main() {
	int input;

	scanf("%d", &input);

	int i;
	for (i = 0; i < input; i++) {
		printf("%d\n", i + 1);
	}

	return 0;
}