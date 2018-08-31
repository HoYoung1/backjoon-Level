#include <stdio.h>

int count[10];

int main() {
	int num;

	scanf("%d", &num);

	while (num) {
		count[num % 10]++;
		num = num / 10;
	}

	int i = 9;
	while (1) {
		if (i < 0) {
			break;
		}
		if (count[i] > 0) {
			printf("%d", i);
			count[i]--;
		}
		else {
			i--;
		}
	}

	return 0;


	
}