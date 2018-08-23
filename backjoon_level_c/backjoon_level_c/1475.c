#include <stdio.h>

int main() {
	int num[10] = { 0, };

	int setCnt = 0;

	int input;

	scanf("%d", &input);

	int i;
	int chk;
	if (input == 0) {
		setCnt = 1;
	}
	while (input) {
		

		chk = input % 10;
		if (num[chk] > 0) {
			num[chk]--;
		}
		else {
			if (chk == 6 && num[9] > 0) {
				num[9]--;
			}
			else if(chk == 9 && num[6] > 0) {
				num[6]--;
			}
			else {
				setCnt++;
				for (i = 0; i < 10; i++) {
					num[i]++;
				}
				num[chk]--;
			}
			
		}
		input = input / 10;
	}
	printf("%d", setCnt);

	return 0;
}