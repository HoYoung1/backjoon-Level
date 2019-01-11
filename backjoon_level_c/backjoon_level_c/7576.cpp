#include <iostream>
#include <vector>
#include <stdio.h>
#include <queue>
using namespace std;

vector<vector<int>> v1;
queue<pair<int, pair<int,int>>> Q;
//Q의 첫번째는 count값 둘째,셋째는 x,y인덱스

int main() {
	v1.assign(1002, vector<int>(1002, -2));

	int M, N;
	scanf("%d%d", &M, &N);
	
	int count0 = 0;
	int chk_count0 = 0;
	int val = 0;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			scanf("%d", &v1[i][j]);
			if (v1[i][j] == 0) {
				count0++;
			}
			else if (v1[i][j] == 1) {
				Q.push(make_pair(0, make_pair(i,j)));
				
			}
		}
	}

	while (!Q.empty()) {
		int x = Q.front().second.first;
		int y = Q.front().second.second;
		val = Q.front().first;
		Q.pop();
		//상 하 좌 우
		if (v1[x - 1][y] == 0) {
			Q.push(make_pair(val + 1, make_pair(x - 1, y)));
			v1[x - 1][y] = 1; 
			chk_count0++;
		}
		if (v1[x + 1][y] == 0) {
			Q.push(make_pair(val + 1, make_pair(x + 1, y)));
			v1[x + 1][y] = 1;
			chk_count0++;
		}
		if (v1[x][y - 1] == 0) {
			Q.push(make_pair(val + 1, make_pair(x , y-1)));
			v1[x][y - 1] = 1;
			chk_count0++;
		}
		if (v1[x][y + 1] == 0) {
			Q.push(make_pair(val + 1, make_pair(x ,y+1)));
			v1[x][y + 1] = 1;
			chk_count0++;
		}
	}
	if (chk_count0 != count0) {
		//전부다 1로 만든것이 아닙니다
		printf("-1");
		return 0;
	}
	printf("%d", val);
	return 0;

}