#include <stdio.h>
#define MAXValue 500

int dp[500][500];

void printDP();

int main() {
	int T;
	scanf("%d", &T); //T는 1에서 500까지 오는것같습니다.

	int **arr;
	arr = (int **)malloc(sizeof(int*)*T);
	for (int i = 0; i < T; i++) { 
		arr[i] = (int *)malloc(sizeof(int)*MAXValue);
	}

	for (int i = 0; i < T; i++) {
		for (int j = 0; j < i + 1; j++) {
			scanf("%d", &arr[i][j]);
		}
	}

	/*for (int i = 0; i < T; i++) {
		for (int j = 0; j < i + 1; j++) {
			printf("%d ", arr[i][j]);
		}

		printf("\n");
	}*/

	dp[0][0] = arr[0][0];
	for (int i = 1; i < T; i++) {
		for (int j = 0; j < i +1; j++) {
			dp[i][j] = arr[i][j]+ max(dp[i - 1][j], dp[i - 1][j - 1],j-1);
		}
	}
	printDP();
	printf("%d", maxNum(dp[T-1],T));




	return 0;
}

int max(int a, int b, int chk) {
	if (chk < 0) {
		return a;
	}
	if (a > b) {
		return a;
	}
	else
		return b;
}

int maxNum(int *p,int T) {
	int maximum = p[0];
	for (int i = 0; i < T; i++) {
		if (maximum < p[i]) {
			maximum = p[i];
		}
	}

	return maximum;
	
}

void printDP() {
	for (int i = 0; i < 500; i++) {
		for (int j = 0; j < 500; j++) {
			printf("%d ", dp[i][j]);
		}
		printf("\n");
	}
}