#include <stdio.h>

int coin[100];
int dp[10001];
//dp[0] = 1로 초기화할것이며 1원일때 경우의수는 dp[1]이다.
//coin[0] = 1, coin[1] = 2 , coin[2] = [5];
int main() {

	int n, k;


	scanf("%d %d", &n, &k);

	for (int i = 0; i < n; i++) {
		scanf("%d", &coin[i]);
	}

	dp[0] = 1;
	for (int i = 0; i < n; i++) {
		for (int j = 1; j < 10001; j++) {
			if(j>=coin[i])
				dp[j] = dp[j] + dp[j - coin[i]];
		}
	}

	printf("%d", dp[k]);
	return 0;
}