//잘하는사람꺼함보자

//버블정렬사용
#include <stdio.h>

int main() {
	int input; 

	int num[1000];

	scanf("%d", &input); // <=1000

	int i,j;
	for (i = 0; i < input; i++) {
		scanf("%d", &num[i]);
	}

	for (i = 0; i < input-1; i++) {
		for (j = 0; j < input-1-i; j++) {
			if (num[j] > num[j+1]) {
				int temp = num[j];
				num[j] = num[j + 1];
				num[j + 1] = temp;
			}
		}
	}

	for (i = 0; i < input; i++) {
		printf("%d\n", num[i]);
	}

	return 0;


}