#include <stdio.h>

int arrfibo[41][2];

void xyfibo(int n); //n은 1부터 n까지의 자연수 , 또는 0 ; return 하는것이 아닌 계산함수임
int printX(int n);
int printY(int n);

int main() {
	//basic setting
	arrfibo[0][0] = 1;
	arrfibo[0][1] = 0;
	arrfibo[1][0] = 0;
	arrfibo[1][1] = 1;
	
	int T;
	scanf("%d", &T);

	int input;
	for (int i = 0; i < T; i++) {
		scanf("%d", &input);
		xyfibo(input);
		printf("%d %d\n", printX(input), printY(input));
	}
	
	

	
	return 0;


}

void xyfibo(int n) {
	if (n < 2)
		return;
	for (int i = 2; i <= n; i++) {
		arrfibo[i][0] = arrfibo[i - 1][0] + arrfibo[i - 2][0];
		arrfibo[i][1] = arrfibo[i - 1][1] + arrfibo[i - 2][1];
	}

}

int printX(int n) {
	return arrfibo[n][0];
}

int printY(int n) {
	return arrfibo[n][1];
}