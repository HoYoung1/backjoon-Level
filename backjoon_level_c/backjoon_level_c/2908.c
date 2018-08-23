#include <stdio.h>

void swap(char *);

int main() {
	char num1[4];
	char num2[4];

	scanf("%s", num1);
	scanf("%s", num2);

	swap(num1);
	swap(num2);
	
	if (atoi(num1) > atoi(num2))
	{
		printf("%s", num1);
	}
	else
	{
		printf("%s", num2);
	}
	
	return 0;

}

void swap(char *a) {
	char temp;
	temp = a[2];
	a[2] = a[0];
	a[0] = temp;
}