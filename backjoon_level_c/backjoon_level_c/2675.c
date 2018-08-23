#include <stdio.h>

int main() {
	int testcase;

	scanf("%d", &testcase);
	int i,j,k;
	int reNum;

	char string[21];
	for (i = 0; i < testcase; i++) {
		scanf("%d",&reNum);
		scanf("%s", string);

		for (j = 0; j < strlen(string); j++) {
			for (k = 0; k < reNum; k++) {
				printf("%c", string[j]);
			}
			
		}
		printf("\n");
		
	}
	return 0;
}