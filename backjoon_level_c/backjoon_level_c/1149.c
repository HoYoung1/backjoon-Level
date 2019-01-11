#include <stdio.h>
#include <stdlib.h>


long long dp[1002][3];

long long minNum(long long a, long long b);
long long min3(long long*);

int main() {
	int T;

	scanf("%d", &T);

	long long **home;
	home = (long long**)malloc(sizeof(long long*)*T);
	for (int i = 0; i < T; i++) {
		home[i] = (long long*)malloc(sizeof(long long) * 3);
	}
	
	

	for (int i = 0; i < T; i++) {
		for (int j = 0; j < 3; j++) {
			scanf("%lld", &home[i][j]);
		}
	}

	//dp에 입력
	dp[0][0] = home[0][0];
	dp[0][1] = home[0][1];
	dp[0][2] = home[0][2];
	for (int i = 1; i < T; i++) {
		for (int j = 0; j < 3; j++) {
			dp[i][j] = home[i][j] + minNum(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]);
		}
	}

	//결과 출력
	printf("%lld", min3(dp[T-1]));


	return 0;


}

long long minNum(long long a, long long b) {
	if (a > b) {
		return b;
	}
	else {
		return a;
	}
}

long long min3(long long* arr) {
	long long minimum = arr[0];
	for (int i = 1; i < 3; i++) {
		if (minimum > arr[i]) {
			minimum = arr[i];
		}
	}
	return minimum;
}
