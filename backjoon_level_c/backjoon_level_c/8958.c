#include <stdio.h>

int main() {
	char strOX[81];

	int num;

	scanf("%d", &num);
	
	int i,j,score,bonus = 0;
	for (i = 0; i < num; i++) {
		scanf("%s", strOX);
		score = 0;
		bonus = 0;
		for (j = 0; j < strlen(strOX); j++) {
			if (strOX[j] == 'O') {
				score = score + 1 + bonus;
				bonus++;
			}
			else {
				bonus = 0;
			}
		
		}
		printf("%d\n", score);
	}

	return 0;

}