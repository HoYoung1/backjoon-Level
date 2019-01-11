#include <stdio.h>
#include <algorithm>

int dp[10000][3]; //dp[x][2]는 현재까지 dp의 최대값임
int wine[10000];

using namespace std;
int main() {
	
	
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%d", &wine[i]);
	}

	dp[0][0] = wine[0];
	dp[0][2] = wine[0];
	dp[1][0] = wine[1];
	dp[1][1] = wine[0] + wine[1];
	dp[1][2] = wine[0] + wine[1];
	

	for (int i = 2; i < T; i++) {
		dp[i][0] = dp[i - 2][2] + wine[i];
		dp[i][1] = dp[i - 1][0] + wine[i];
		dp[i][2] = max(dp[i - 1][2], max(dp[i][0], dp[i][1]));
	}

	printf("%d", dp[T-1][2]);
	return 0;
}