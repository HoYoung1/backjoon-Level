#include <stdio.h>

int main() {

	int num[8] = {0,};

	

	int i;
	for (i = 0; i < 8; i++) {
		scanf("%d", &num[i]);
	}
	int checkNum;
	if (num[0] == 1) {
		checkNum = 1;
		for (i = 0; i < 8; i++) {
			if (num[i] != checkNum) {
				printf("mixed");
				return 0;
			}
			checkNum++;
		}
		printf("ascending");
	}
	else if (num[0] == 8) {
		checkNum = 8;
		for (i = 0; i < 8; i++) {
			if (num[i] != checkNum) {
				printf("mixed");
				return 0;
			}
			checkNum--;
		}
		printf("descending");
	}
	else {
		printf("mixed");
	}

	return 0;

	
}