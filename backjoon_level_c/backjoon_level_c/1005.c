#include <stdio.h>



int main() {
	int T;

	scanf("%d", &T);

	int N, K;
	for (int i = 0; i < T; i++) {
		

		scanf("%d %d", &N, &K);

		int *buildingT = (int*)malloc(sizeof(int)*N);
		for (int j = 0; j < N; j++) {
			scanf("%d", &buildingT[j]);
			
		}
		int **arr = (int**)malloc(sizeof(int*)*N);
		for (int j = 0; j < N; j++) {
			arr[j] = (int*)malloc(sizeof(int)*N);

		}
		for (int j = 0; j < K; j++) {
			int a, b;
			scanf("%d %d", &a, &b);
			arr[a-1][b-1] = 1;
		}

		int last;
		scanf("%d", &last);
		//출력확인,필요없음
		/*for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				printf("%d ", arr[i][j]);
			}
			printf("\n");
		}*/
	}

	
	return 0;
}