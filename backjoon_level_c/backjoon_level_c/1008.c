#include <stdio.h>

double div(int, int);
int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%0.32lf", div(a, b));
}

double div(int a, int b) {
	return (double)a / (double)b;
}