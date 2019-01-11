#include <stdio.h>

int factorial(int n) {
	if (n == 1) {
		return 1;
	}
	return n * factorial(n - 1);
}
int main() {
	int a, b;

	scanf("%d %d", &a, &b);
	printf("%d", factorial(a) / factorial(a-b));
	return 0;
}