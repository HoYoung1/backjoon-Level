#include <stdio.h>

int mul(int a, int b);
int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", mul(a, b));

}

int mul(int a, int b) {
	return a * b;
}