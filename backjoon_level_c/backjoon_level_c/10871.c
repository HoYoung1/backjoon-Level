#include <stdio.h>
#include <stdlib.h>

int main() {

	int size, num;
	scanf("%d %d", &size, &num);
	printf("num : %d\n", num);
	int *arr;

	arr = (int*)malloc(sizeof(int)*size);

	int i;
	for (i = 0; i < size; i++) {
		scanf("%d", &arr[i]);
		if (arr[i] < num)
		{
			printf("%d ", arr[i]);
		}
	}
	free(arr);
}