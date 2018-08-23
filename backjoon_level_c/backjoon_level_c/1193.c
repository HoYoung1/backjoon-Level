#include <stdio.h>

int main() {
	int a = 1 ,b = 2;

	int cal = 1;
	
	int input;
	scanf("%d", &input);

	int i,group=1;
	if (input == 1) {
		printf("1/1");
		return 0;
	}
	for (i = 2; i < input; i++) {
		a = a + cal;
		b = b + cal * -1;

		if (a == 0) {
			a = 1;
			cal = cal * -1;
		}
		else if (b == 0) {
			b = 1;
			cal = cal * -1;
		}

	}

	printf("%d/%d", a, b);
	return 0;


}