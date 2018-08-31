#include <stdio.h>

int main() {
	
	int N;
	int num;
	int primeCnt=0;

	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%d", &N);
		
		int cnt=0;
		int val = N;
		if (N > 2 && N % 2 == 0) {
			continue;
		}
		while (N) {
			if (val % N-- == 0) {
				cnt++;
				if (cnt > 2) {
					break;
				}
			}
		}
		if (cnt == 2) {
			primeCnt++;
		}

	}
	printf("%d", primeCnt);
	return 0;
}