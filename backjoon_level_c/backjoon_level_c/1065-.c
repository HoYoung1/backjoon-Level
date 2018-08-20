#include <stdio.h>
int hansu(int);

int main() {
	int input;

	scanf("%d", &input);
	printf("%d", hansu(input));
	
	return 0;

}

int hansu(int n) {
	int cnt = 0;

	if (n < 100) {
		return n;
	}
	else {
		if (n == 1000) {
			n = 999;
		}
		int pos[4];
		int i,j=0;
		
	

		for (i = 100; i <= n; i++) {
			int num = i;
			j = 0;
			while (num) {
				pos[j] = num % 10;
				num = num / 10;
				j++;
			}
			//printf("pos 0 : %d\n", pos[0]);
			//printf("pos 1 : %d\n", pos[1]);
			//printf("pos 2 : %d\n", pos[2]);

			if (pos[1] - pos[0] == pos[2] - pos[1]) {
				//한수입니다.
				cnt++;
			}
		}
	}
	return 99+cnt;
}