#include <stdio.h>

int num[1000000];
void quicksort(int*, int, int);

int main() {
	int N;
	
	scanf("%d", &N);

	int i;

	for (i = 0; i < N; i++) {
		scanf("%d", &num[i]);
	}

	quicksort(num, 0, N - 1);

	for (i = 0; i < N; i++) {
		printf("%d\n", num[i]);
	}

	return 0;
}

void quicksort(int *arr, int start, int end) {
	if (start > end) {
		return;
	}

	int pivot = start;

	int i = start + 1;
	int j = end;
	int temp;

	while (arr[pivot] > arr[i]) {
		i++;
	}

	while (arr[pivot] < arr[j]) {
		j++;
	}

	if (i > j) {
		temp = arr[pivot];
		arr[pivot] = arr[j];
		arr[j] = temp;
	}//¾ù°¥·È´Ù¸é
	else {
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	quicksort(arr, start, j - 1);
	quicksort(arr, j + 1, end);
}