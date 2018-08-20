#include <stdio.h>

int main() {
	int cycle=0;

	int input;

	scanf("%d", &input);

	int one, ten; //1의자리 10의자리
	int newNum = input; // 새로운 수
	while (1) {
		
		cycle++;
		one = newNum % 10;
		ten = newNum / 10;
		
		newNum = one*10 + (ten+one)%10;

		if (input == newNum) {
			break;
		}
		
	}
	printf("%d", cycle);

	return 0;
}