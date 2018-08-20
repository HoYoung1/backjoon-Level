#include <stdio.h>
#include <stdlib.h>

int main() {
	int testcase;

	scanf("%d", &testcase);

	int i, j;
	int cnt;
	int *arr;
	float avr;

	for (i = 0; i < testcase; i++) {
		scanf("%d", &cnt);
		arr = (int*)malloc(sizeof(int)*cnt);
		int sum = 0;
		for (j = 0; j < cnt; j++) {
			scanf("%d", &arr[j]);
			sum = sum + arr[j];
		}
		avr = sum / (float)cnt ; //Æò±Õ°ª

		//printf("avr : %f\n", avr);

		int higherCnt = 0;
		for (j = 0; j < cnt; j++) {
			if (arr[j] > avr) {
				higherCnt++;
			}
		}
		//printf("highercnt : %d\n", higherCnt);
		printf("%.3f%%\n", higherCnt / (float)cnt * 100);



		free(arr);
	}

	return 0;
}