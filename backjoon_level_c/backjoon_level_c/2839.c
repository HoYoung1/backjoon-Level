#include <stdio.h>

int num_of_bag(int);
int main() {
	int Nkg;

	scanf("%d", &Nkg);

	printf("%d", num_of_bag(Nkg));
	return 0;
}

int num_of_bag(int Nkg) {
	int num_of_five, num_of_three;

	num_of_five = Nkg / 5;
	while (1) {
		if (num_of_five < 0) {
			return -1;
		}
		if ((Nkg - (num_of_five * 5)) % 3 == 0) {
			num_of_three = (Nkg - (num_of_five * 5)) / 3;
			break;
		}
		num_of_five--;
	}
	return num_of_five + num_of_three;
}