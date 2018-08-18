/*
#include <stdio.h>

int main() {
	int num;
	int input;

	scanf("%d", &num);
	
	scanf("%d", &input);

	int pos=1;
	int sum = 0;
	int i;

	for (i = 1; i < num; i++)
	{
		pos = pos * 10;
	}

	for (i = 0; i < num; i++)
	{
		sum = sum + (input / pos);
		input = input - (input / pos) * pos;
		printf(" input : %d \n ", input);
		pos = pos / 10;
	}

	printf("%d", sum);
	return 0; 


}
*/

#include <stdio.h>

int main() {
	int size;
	int sum = 0;

	scanf("%d", &size);

	char *arrNum;

	arrNum = (char*)malloc(sizeof(char)*size);

	while (getchar() != '\n');

	int i;
	for (i = 0; i < size; i++) {
		scanf("%c", &arrNum[i]);
		//printf("%d", arrNum[i] - '0');
		sum = sum + (arrNum[i]-'0');
	}
	free(arrNum);
	printf("%d", sum);
	return 0;

}