#include <stdio.h>

int main() {
	int num[3];

	int i, j;

	for (i = 0; i < 3; i++) {
		scanf("%d", &num[i]);
	}

	int temp;
	for (i = 0; i < 3 - 1; i++) {
		for (j = 0; j<3 - 1; j++)
			if (num[j + 1] < num[j]) {
				temp = num[j];
				num[j] = num[j + 1];
				num[j + 1] = temp;
			}
	}


	printf("%d", num[1]);


	return 0;
}