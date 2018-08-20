#include <stdio.h>

int main() {
	int num[3];
	int cntArr[10] = {0};
	int mulNum;

	int i;
	for (i = 0; i < 3; i++) {
		scanf("%d", &num[i]);
	}

	mulNum = num[0] * num[1] * num[2];

	int n = mulNum;

	while (n) {
		cntArr[n % 10]++;
		n = n / 10;
	}



	for (i = 0; i < sizeof(cntArr) / sizeof(int); i++) {
		printf("%d\n", cntArr[i]);
	}

	return 0;
	
	
}