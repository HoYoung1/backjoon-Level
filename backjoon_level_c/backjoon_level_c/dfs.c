

#include <stdio.h>

#define MAXSIZE 1001

int DFSvisited[MAXSIZE];
int BFSvisited[MAXSIZE];

int maps[MAXSIZE][MAXSIZE];
int queue[MAXSIZE];

int main() {
	int v, n, startV;
	scanf("%d %d %d", &v, &n, &startV);
	
	for (int i = 0; i < n; i++) {
		int vv, ii;
		scanf("%d %d", &vv, &ii);

		maps[vv][ii] = 1;
		maps[ii][vv] = 1;
	}
	DFS(startV,MAXSIZE);
	printf("\n");
	BFS(startV, MAXSIZE);

	return 0;
}

int DFS(int v, int N) {
	//DFS는 재귀 사용
	DFSvisited[v] = 1;
	printf("%d ", v);
	for (int i = 1; i <= N; i++) {
		if (DFSvisited[i] == 0 && maps[v][i] == 1) {
			DFS(i, N);
		}
	}
}

int BFS(int v, int N) {
	int front=0, rear = 0;

	//BFS는 큐 사용
	
	
	
	queue[rear] = v;
	rear++;
	BFSvisited[v] = 1;

	while (front < rear) {
		
		int vv = queue[front];
		front++;
		printf("%d ", vv);
		for (int i = 1; i <= N; i++) {
			if (BFSvisited[i] == 0 && maps[vv][i] == 1) {
				
				queue[rear] = i;
				rear++;
				BFSvisited[i] = 1;
			}
		}
	}
	
}