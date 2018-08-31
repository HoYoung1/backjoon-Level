#include <stdio.h>

int prime[1000001];

int main() {
	int M;
	int N;
	scanf("%d", &M);
	scanf("%d", &N);

	//prime[1] = 숫자 1 의미 
	for (int i = 2; i < 1000001; i++) {
		if (prime[i] == -1) {
			continue;
		}
		int primeNum = i;
	/*	while (j) {
			if (i%j-- == 0) {
				cnt++;
				if (cnt > 2) {
					break;
				}
			}
		}*/
	
		
		//소수 입니다. 
		//printf("소수입니다 : %d\n", i);
		prime[i] = 1;

		//에라토스테네스의 체를 이용하여 배수를 모두 -1로 변경
		int k = 2;
		int chk = i * k;
		while (chk<1000001) {
			prime[chk] = -1;
			k++;
			chk = i * k;
		}
			
		
		
	}
	for (int i = M; i <= N; i++) {
		if (prime[i] == 1) {
			printf("%d\n", i);
		}
	}

	return 0;

}