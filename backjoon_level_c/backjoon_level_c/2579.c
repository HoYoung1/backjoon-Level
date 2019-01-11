//#include <stdio.h>
//
//int stair[300];
//int dp[300][2];
//
//int maxchk(int,int ,int );
//int main() {
//
//
//	int T;
//	scanf("%d", &T);
//
//	for (int i = 0; i < T; i++) {
//		scanf("%d", &stair[i]);
//	}
//
//	dp[0][0] = stair[0];
//	dp[0][1] = stair[0];
//	int dp0cnt = 0;
//	int dp1cnt = 0;
//
//	dp[1][0] = dp[0][0] + stair[1];
//	dp0cnt = 1;
//	dp[1][1] = dp[0][0];
//	dp1cnt = 0;
//	for (int i = 2; i < T; i++) {
//		if (dp0cnt == 2) {
//			dp[i][0] = dp[i - 1][0];
//			dp0cnt = 0;
//		}
//		else {
//			dp[i][0] = dp[i - 1][0] + stair[i];
//			dp0cnt++;
//
//		}
//
//		if (dp1cnt == 2) {
//			dp[i][1] = dp[i - 1][1];
//			dp1cnt = 0;
//		}
//		else {
//			dp[i][1] = dp[i - 1][1] + stair[i];
//			dp1cnt++;
//
//		}
//	}
//
//	printf("%d", maxchk(T, dp0cnt, dp1cnt));
//
//	return 0;
//}
//
//int maxchk(int t,int chk1, int chk2) {
//	if (chk1 == 0) {
//		return dp[t - 1][1];
//	}
//	else if (chk2 == 0) {
//		return dp[t - 1][0];
//	}
//
//
//	if (dp[t - 1][0] > dp[t - 1][1]) {
//		return dp[t - 1][0];
//	}
//	else {
//		return dp[t - 1][1];
//	}
//}

//#include <stdio.h>
//#include <stdlib.h>
//
//#define max(a,b) (((a)>(b)) ? (a):(b))
//int dp[300][2];
//int maxchk(int t, int chk1, int chk2, int *stair);
////[][0]:첫계단 밟을때 //[][1]:안밟을때
//
//int main() {
//
//	
//	int T; // 300이하의 자연수
//
//	int *stair;
//	scanf("%d", &T);
//
//	stair = (int*)malloc(sizeof(int)*T);
//
//	for (int i = 0; i < T; i++) {
//		scanf("%d", &stair[i]);
//	}
//
//	dp[0][0] = stair[0];
//	dp[1][0] = stair[0] + stair[1];
//	
//	dp[1][1] = stair[1];
//	int dp0cnt = 2;
//	int dp1cnt = 1;
//
//	for (int i = 2; i < T; i++) {
//		if (dp0cnt == 2) {
//			if (dp[i - 1][0] > dp[i - 2][0] + stair[i]) {
//				dp0cnt = 0;
//				dp[i][0] = dp[i - 1][0];
//			}
//			else {
//				dp[i][0] = dp[i - 2][0] + stair[i];
//				dp0cnt = 1;
//			}
//		}
//		else {
//			if ((dp[i - 1][0] + stair[i]) > dp[i - 2][0] + stair[i]) {
//				dp[i][0] = (dp[i - 1][0] + stair[i]);
//				dp0cnt = 2;
//			}
//			else {
//				dp[i][0] = dp[i - 2][0] + stair[i];
//				dp0cnt = 1;
//			}
//		}
//
//
//
//
//
//		if (dp1cnt == 2) {
//			if (dp[i - 1][1] > dp[i - 2][1] + stair[i]) {
//				dp1cnt = 0;
//				dp[i][1] = dp[i - 1][1];
//			}
//			else {
//				dp[i][1] = dp[i - 2][1] + stair[i];
//				dp1cnt = 1;
//			}
//		}
//		else {
//			if ((dp[i - 1][1] + stair[i]) > dp[i - 2][1] + stair[i]) {
//				dp[i][1] = (dp[i - 1][1] + stair[i]);
//				dp1cnt = 2;
//			}
//			else {
//				dp[i][1] = dp[i - 2][1] + stair[i];
//				dp1cnt = 1;
//			}
//		}
//	}
//	printf("%d", maxchk(T,dp0cnt,dp1cnt,stair));
//	return 0;
//}
//
//int maxchk(int t,int chk1,int chk2,int *stair) {
//	if (chk1 ==0 && chk2==0)
//		return max(dp[t - 3][0] + stair[t - 1], dp[t - 3][1] + stair[t - 1]);
//	if (dp[t - 1][0] > dp[t - 1][1] && chk1 !=0)
//		return dp[t - 1][0];
//	else
//		return dp[t - 1][1];
//}

#include <stdio.h>
//#define max(a,b) (((a)>(b)) ? (a): (b))
int max(int, int);
int stair[301];
int dp[301][2];
int main() {

	int T;
	scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		scanf("%d", &stair[i]);

	}
	//1번 계단부터 300번 계단 까지 들어갈 수 있습니다.

	dp[0][0] = 0;
	dp[0][1] = 0;
	dp[1][0] = stair[1];
	dp[1][1] = stair[1];
	dp[2][0] = stair[2];
	dp[2][1] = stair[1] + stair[2];

	for (int i = 3; i <= T; i++) {
		dp[i][0] = max(dp[i - 2][0], dp[i - 2][1])+ stair[i];
		dp[i][1] = dp[i - 1][0] + stair[i];
	}

	printf("%d", max(dp[T][0], dp[T][1]));
	


	return 0;
}

int max(int a, int b) {
	if (a > b)
		return a;
	return b;
}