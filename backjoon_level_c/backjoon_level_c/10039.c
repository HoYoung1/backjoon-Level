#include <stdio.h>

int main() {
	int score[5];

	int i;
	for (i = 0; i < 5; i++) {
		scanf("%d", &score[i]);
		if (score[i] < 40) {
			score[i] = 40;
		}
	}

	int sum=0;
	for (i = 0; i < 5; i++) {
		sum = sum + score[i];
	}

	printf("%d", sum / 5);
	return 0;

	
}