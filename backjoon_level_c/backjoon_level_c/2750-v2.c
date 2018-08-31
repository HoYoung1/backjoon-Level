#include <stdio.h>

int main() {
	int input;
	int num[1000];

	scanf("%d", &input);

	int i,j;
	for (i = 0; i < input; i++) {
		scanf("%d", &num[i]);
	}

	//선택정렬시작

	for (i = 0; i < input; i++) {
		for (j = i + 1; j < input; j++) {
			if (num[i] > num[j]) {
				int temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
		}
	}

	for (i = 0; i < input; i++) {
		printf("%d\n", num[i]);
	}

	return 0;
}
