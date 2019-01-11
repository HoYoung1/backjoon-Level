//#include <stdio.h>
//
//
//int chk[10];
//int result[10];
//
//int resultV;
//
//int sum(int *arr);
//int main() {
//	
//	int input;
//	scanf("%d", &input);
//
//	int n = input;
//	//n=1 
//	for (int i = 1; i < 10; i++) {
//		chk[i] = 1;
//	}
//	if (n == 1)
//		resultV = 10;
//	else {
//		while (n != 1) {
//			n--;
//			for (int i = 0; i < 10; i++) {
//				while (chk[i]>0) {
//					if (i >= 1 && i <= 8) {
//						result[i - 1]++;
//						result[i + 1]++;
//					}
//					//i가 0이거나 9라면
//					else {
//						if (i == 0)
//							result[i + 1]++;
//						else //i가 9라면
//							result[i - 1]++;
//					}
//					chk[i]--;
//				}
//			}
//			
//			//그대로 옮겨준다
//			for (int i = 0; i < 10; i++) {
//				chk[i] = result[i];
//				result[i] = 0;
//			}
//
//		}
//		resultV = sum(chk);
//	}
//	printf("%d", resultV % 1000000000);
//
//	return 0;
//		
//}
//
//int sum(int *arr) {
//	int sum = 0;
//	for (int i = 0; i < 10; i++) {
//		sum = sum + arr[i];
//	}
//	return sum;
//}



#include <stdio.h>

long long N[13][103];
long long sum(int n);

int main() {

	int input;
	scanf("%d", &input);

	for (int i = 2; i < 11; i++) {
		N[i][1] = 1;
	}

	for (int i = 2; i < 101; i++) {
		for (int j = 1; j < 11; j++) {
			N[j][i] = (N[j - 1][i - 1] + N[j + 1][i - 1]) % 1000000000;
		}
	}

	printf("%lld", sum(input)% 1000000000);


	return 0;
}

long long sum(int n) {
	long long sum = 0;
	for (int i = 1; i < 11; i++) {
		sum = sum + N[i][n];
	}
	return sum;
}