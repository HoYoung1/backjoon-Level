//#include <stdio.h>
//
//int main() {
//	int fiboNum;
//	scanf("%d", &fiboNum);
//
//	printf("%d", fibo(fiboNum));
//	return 0;
//}
//
//
//int fibo(int n) {
//	if (n == 0) {
//		return 0;
//	}
//	else if (n == 1) {
//		return 1;
//	}
//
//	return fibo(n - 1) + fibo(n - 2);
//}

#include <stdio.h>



int main() {
	int fiboNum;

	long long fibo[100];


	scanf("%d", &fiboNum);

	fibo[0] = 0;
	fibo[1] = 1;
	
	for (int i = 0; i < fiboNum; i++) {
		fibo[i + 2] = fibo[i + 1] + fibo[i];
	}


	

	
	printf("%lld", fibo[fiboNum]);
	return 0;
}