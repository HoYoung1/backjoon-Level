#include <stdio.h>

int main() {
	char a[100];

	while (scanf("%[^\n]s",a) != EOF) {
		printf("%s\n", a);
		while (getchar() != '\n');
	}
	return 0;
}