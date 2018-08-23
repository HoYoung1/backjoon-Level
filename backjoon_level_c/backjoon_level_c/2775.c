#include <stdio.h>

int main() {
	int apart[15][15];

	int i, j,k;
	//0Ãþ ¼ÂÆÃ
	for (i = 0; i < 14; i++) {
		apart[0][i] = i+1;
	}

	//1ÃþºÎÅÍ¼ÂÆÃ
	for (i = 1; i < 15; i++) {
		for (j = 0; j < 15; j++) {
			int sum = 0;
			for (k = 0; k < j+1; k++) {
				sum = sum + apart[i - 1][k];
				apart[i][j] = sum ;
			}
		
		}
	}

	/*for (i = 0; i < 14; i++) {
		for (j = 0; j < 14; j++) {
			printf("%d ", apart[i][j]);
		}
		printf("\n");
	}*/
	int testcase;
	scanf("%d", &testcase);
	int a, b;
	for (i = 0; i < testcase; i++) {
		scanf("%d %d", &a, &b);

		printf("%d\n", apart[a][b-1]);
	}
	return 0;
}