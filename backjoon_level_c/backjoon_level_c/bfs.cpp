#include <iostream>
#include <vector>
#include <queue>


//ÀÔ·Â°ª
//0 1
//1 2
//1 3
//2 4
//3 5
//3 6
//5 7
using namespace std;

int visited[8] = { 0, };

int bfs(int graph[][8], int start, int end) {
	queue<pair<int,int>> Q;
	Q.push(pair<int,int>(start,0));
	visited[start] = 1;
	int count = 1;

	while (!Q.empty()) {
		int num = Q.front().first;
		int second = Q.front().second;
		Q.pop();
		for (int i = 0; i < 8; i++) {
			if (visited[i] == 0 && graph[num][i] == 1) {
				Q.push(pair<int,int>(i,second+1));
				if (i == end)
					return second+1;
			}
		}
		count++;
	}

	return -1;
}
int main() {
	int graph[8][8] = {0,};

	for (int i = 0; i < 7; i++) {
		int n, m;
		scanf("%d%d", &n, &m);
		graph[n][m] = 1;
		graph[m][n] = 1;
	}

	cout << bfs(graph, 3, 7);

	return 0;
}