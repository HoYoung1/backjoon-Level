#include <stdio.h>

int main() {
	int M;
	int N;

	scanf("%d", &M);
	scanf("%d", &N);

	int sum = 0;
	int min = 0;
	for (int i = M; i <= N; i++) {
		int j = i;
		int cnt = 0;
		while (j) {
			if (i%j-- == 0) {
				cnt++;
				if (cnt > 2) {
					break;
				}
			}
		}
		if (cnt == 2) {
			//i�� �Ҽ��Դϴ�.
			sum = sum + i;
			if (min == 0) {
				//���� �ּҰ� ���ٴ� ��
				min = i;
			}
		}
		
		
		
	}
	if (sum == 0) {
		printf("-1");
	}
	else {
		printf("%d\n", sum);
		printf("%d\n", min);
	}


	return 0;
}