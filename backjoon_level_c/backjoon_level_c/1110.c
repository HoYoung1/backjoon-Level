#include <stdio.h>

int main() {
	int cycle=0;

	int input;

	scanf("%d", &input);

	int one, ten; //1���ڸ� 10���ڸ�
	int newNum = input; // ���ο� ��
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