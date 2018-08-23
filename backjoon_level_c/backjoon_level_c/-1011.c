#include <stdio.h>
int main() {
	int testcase;
	scanf("%d", &testcase);
	long long i,j;
	long long k , cnt , flag , temp;
	long long t ;
	int a, b;
	for (t = 0; t < testcase; t++) {
		scanf("%d%d", &a, &b);
		long long int num = b - a;

		i = 2;
		j = 2;
		cnt = 0, flag = 1, temp = 0;
		if (num == 1) {
			j = 1;
		}
		else {
			while (i<num) {
				if (cnt > 0) {
					j--;
					cnt--;
				}
				else if (flag == 0 && cnt == 0) {
					flag = 1;
					cnt = temp;
				}
				else if (flag == 1 && cnt == 0) {
					flag = 0;
					temp++;
					cnt = temp;
				}
				j++;
				i++;
			}
		}
		printf("%d\n", j);
	}
	return 0;
}