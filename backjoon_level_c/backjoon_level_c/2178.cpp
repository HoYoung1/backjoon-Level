#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <queue>
using namespace std;

vector<vector<int>> v1;
vector<vector<int>> visited;
queue<pair<int,pair<int,int>>> Q;

int main() {
	v1.assign(102, vector<int>(102, -1));
	visited.assign(102, vector<int>(102, 0));

	int N, M;

	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		string s;
		cin >> s;

		int stringSize = s.size();
		for (int j = 1; j <= stringSize; j++) {
			v1[i][j] = s[j-1]-'0';
		}
	}

	
	Q.push(make_pair(1, make_pair(1, 1)));
	visited[1][1] = 1;
	while (!Q.empty()) {
		int a = Q.front().first; // ��
		int b = Q.front().second.first; //��
		int minDay = Q.front().second.second; //������ġ�� �ּ� ����ĭ��

		Q.pop();

		if (a == N && b == M) {
			//ã�� �� �Դϴ�.
			cout << minDay;
			break;
		}

		//��, �Ʒ� , ����,������ ���� ������.
		
		//��
		if (v1[a - 1][b] == 1 && visited[a - 1][b] == 0) {
			Q.push(make_pair(a-1, make_pair(b, minDay + 1)));
			visited[a - 1][b] = 1;
		}

		//�Ʒ�
		if (v1[a + 1][b] == 1 && visited[a + 1][b] == 0) {
			Q.push(make_pair(a + 1, make_pair(b, minDay + 1)));
			visited[a+1][b] = 1;
		}

		//����
		if (v1[a][b-1] == 1 && visited[a][b - 1] == 0) {
			Q.push(make_pair(a, make_pair(b-1, minDay + 1)));
			visited[a][b-1] = 1;
		}

		//������
		if (v1[a ][b+1] == 1 && visited[a][b+1] == 0) {
			Q.push(make_pair(a, make_pair(b+1, minDay + 1)));
			visited[a][b+1] = 1;
		}

	}

	return 0;
}
