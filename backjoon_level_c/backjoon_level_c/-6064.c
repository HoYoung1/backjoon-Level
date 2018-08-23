#include <stdio.h>

int main() {
	int M, N, x, y;

	int testcase;
	int cnt;
	scanf("%d", &testcase);

	int i;
	for (i = 0; i < testcase; i++) {
		scanf("%d%d%d%d", &M, &N, &x, &y);

		cnt = 0;
		int flag = 0;
		while (1) {
			if (cnt > M) {
				printf("-1\n");
				flag = 1;
				break;
			}
			if ((x + M * cnt) % M == x) {
				if ((x + M * cnt) % N == y)
					break;
			}
			
			


			cnt++;
		}

		if(flag == 0)
			printf("%d\n", cnt*M+x);



		
		
	}
	return 0;
}
