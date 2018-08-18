#include <stdio.h>
#include <string.h>

int main() {
	char c;

	int count = 0;
	while (scanf("%c", &c) != EOF) {
		
		printf("%c", c);
		count++;
		if (count % 10 ==0) {
			printf("\n");
		}
	}
	return 0;
}
