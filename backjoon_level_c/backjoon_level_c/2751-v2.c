#include <stdio.h>

int sorted[1000000];

int merge(int a[], int m, int middle, int n);
int mergesort(int[],int,int);

int main() {
	
	int input;
	scanf("%d", &input);

	int i;
	int *arr = (int*)malloc(sizeof(int)*input);
	for (i = 0; i < input; i++) {
		scanf("%d", &arr[i]);
	}

	mergesort(arr, 0, input - 1);

	for (i = 0; i < input; i++) {
		printf("%d\n", arr[i]);
	}
	
}

int merge(int a[], int m, int middle, int n) {
	int i = m;
	int j = middle + 1;
	int k = m;

	//정렬된 두 배열을 합침
	while (i <= middle && j <= n)
	{
		if (a[i] <= a[j]) {
			sorted[k] = a[i];
			i++;
		}
		else {
			sorted[k] = a[j];
			j++;
		}
		k++;
	}

	//나머지값을 배열에 넣음.
	if (i > middle) {
		for (int t = j; t <=n; t++) {
			sorted[k] = a[t];
			k++;
	
		}
	}
	else {
		for (int t = i; t <=middle; t++) {
			sorted[k] = a[t];
			k++;
			
		}
	}

	//정렬된 배열로 합치기.
	for (int t = m; t <=n; t++) {
		a[t] = sorted[t];
	}

}

int mergesort(int a[], int m, int n) {
	
	//n이 더 커야한다, 즉 1개보다 커야함
	if (m < n) {
		int middle = (m + n) / 2;
		mergesort(a, m, middle);
		mergesort(a, middle + 1, n);
		merge(a, m, middle, n);
	}
}