#include <stdio.h>

int prime[1000001];

int main() {
	
	

	//prime[1] = ���� 1 �ǹ� 
	for (int i = 2; i < 1000001; i++) {
		if (prime[i] == -1) {
			continue;
		}
		int primeNum = i;

		prime[i] = 1;

		//�����佺�׳׽��� ü�� �̿��Ͽ� ����� ��� -1�� ����
		int k = 2;
		int chk = i * k;
		while (chk<1000001) {
			prime[chk] = -1;
			k++;
			chk = i * k;
		}



	}

	int input;
	while (1) {
		scanf("%d", &input);

		if (input == 0) {
			break;
		}
		int cnt = 0;
		for (int i = input+1; i <= input * 2; i++) {
			if (prime[i] == 1)
				cnt++;
		}
		printf("%d\n", cnt);
	}

	return 0;

}