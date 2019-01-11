#include <stdio.h>



int dp[1000001];

int minRecur(int n);

int main() {
	int input;


	scanf("%d", &input);

	for (int i = 1; i <= input; i++) {
		dp[i] = -1;
	}
	printf("%d", minRecur(input));

	return 0;
	 

}

int minRecur(int n) {
	if (n == 1) {
		return 0;
	}
	
	if (dp[n] == -1) {
		if (n % 3 == 0 && n % 2 == 0) {
			dp[n] = min3(minRecur(n - 1), minRecur(n / 3), minRecur(n / 2));
			dp[n] = dp[n] + 1;
		}
		else if (n % 3 == 0 && n % 2 != 0) {
			dp[n] = min2(minRecur(n - 1), minRecur(n / 3));
			dp[n] = dp[n] + 1;
		}
		else if (n % 3 != 0 && n % 2 == 0) {
			dp[n] = min2(minRecur(n - 1), minRecur(n / 2));
			dp[n] = dp[n] + 1;
		}
		else {
			dp[n] = minRecur(n - 1);
			dp[n] = dp[n] + 1;
		}
		
	}
	return dp[n];
	
	
	

}

int min3(int a, int b, int c) {
	
	int min = min2(a, b);
	if (c < min) {
		min = c;
	}
	return min;
}

int min2(int a, int b) {
	if (a > b)
		return b;
	else
		return a;
}