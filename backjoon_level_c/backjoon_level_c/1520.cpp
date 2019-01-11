//#include <cstdio>
//#include <stdlib.h>
//
//void dfs(int **arr, int **visited, int n, int m);
//
//int count = 0;
//int N, M;
//int main() {
//	
//
//	scanf("%d %d", &N, &M);
//
//	int **arr = (int**)malloc(sizeof(int*)*N);
//	int **visited = (int**)malloc(sizeof(int*)*N);
//	for (int i = 0; i < M; i++) {
//		arr[i] = (int*)malloc(sizeof(int)*M);
//		visited[i] = (int*)malloc(sizeof(int)*M);
//	}
//
//	for (int i = 0; i < N; i++) {
//		for (int j = 0; j < M; j++) {
//			scanf("%d", &arr[i][j]);
//			visited[i][j] = 0;
//		}
//	}
//
//	dfs(arr,visited,0,0);
//	printf("%d", count);
//
//	return 0;
//}
//
//void dfs(int **arr, int **visited,int n, int m) {
//	
//	//�������� �����ߴٸ� ī��Ʈ ������ back
//	if (n == (N - 1) && m == (M - 1)) {
//		count++;
//		return;
//	}
//
//	//�Ʒ� ������ ���� ���� ������ Ȯ������
//	
//	//�Ʒ�
//	if (n + 1 < N && visited[n + 1][m] != 1) {
//		if (arr[n + 1][m] < arr[n][m]) {
//
//			visited[n][m] = 1;
//			dfs(arr, visited,n + 1, m);
//			visited[n][m] = 0;
//		}
//	}
//	
//	if (m + 1 < M && visited[n][m + 1] != 1) {
//		if (arr[n][m + 1] < arr[n][m]) {
//			//�����U
//			visited[n][m] = 1;
//			dfs(arr, visited, n, m + 1);
//			visited[n][m] = 0;
//		}
//	}
//
//	if (m - 1 >= 0 && visited[n][m-1] != 1) {
//		if (arr[n][m-1] < arr[n][m]) {
//			//�ަU
//			visited[n][m] = 1;
//			dfs(arr, visited, n, m - 1);
//			visited[n][m] = 0;
//		}
//	}
//	
//	if (n - 1 >= 0 && visited[n - 1][m] != 1) {
//		if (arr[n - 1][m] < arr[n][m] && n - 1 >= 0) {
//			//����
//			visited[n][m] = 1;
//			dfs(arr, visited, n - 1, m);
//			visited[n][m] = 0;
//		}
//	}
//	
//}

//�ð� �ʰ� �ڵ��Դϴ�. 
//�ٽ� ¥����


#include <cstdio>
#include <cstdlib>

int memo(int n, int m);

int count = 0;
int N, M;
int dp[502][502];
int arr[502][502];

int main() {

	scanf("%d %d", &N, &M);
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			scanf("%d", &arr[i][j]);
			dp[i][j] = -1;
		}
	}

	dp[1][1] = 1;

	printf("%d", memo(N,M));
	
		

	return 0;
}

int memo(int n, int m) {
	
	//���ŵǾ��ִ°��̶�� 
	if (dp[n][m] != -1)
		return dp[n][m];
	if (n == 1 && m == 1)
		return dp[1][1];
		
	int sum=0;
	if (arr[n][m] < arr[n - 1][m])
		sum = sum + memo(n - 1, m); //����
	if(arr[n][m]<arr[n+1][m])
		sum = sum + memo(n + 1, m); //�Ʒ���
	if(arr[n][m]<arr[n][m-1])
		sum = sum + memo(n, m-1); //����
	if(arr[n][m]<arr[n][m+1])
		sum = sum + memo(n , m+1); // ����

	dp[n][m] = sum;
	return dp[n][m];
}
