#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

vector<int> vHouse;
vector<vector<int>> v1;
vector<vector<int>> visited;
queue<pair<int, int>> Q;
int main() {
	int num_of_group = 0;

	v1.assign(27, vector<int>(27, -1));
	visited.assign(27, vector<int>(27, 0));

	int N;
	cin >> N;


	for (int i = 1; i <= N; i++) {
		string s;
		cin >> s;
		for (int j = 1; j <= s.size(); j++) {
			v1[i][j] = s[j-1]-'0';
		}
	}

	//���μ�ȯ
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (v1[i][j] == 1 && visited[i][j] == 0) {
				
				num_of_group++;
				visited[i][j] = num_of_group;
				
				//q���ְ�
				Q.push(make_pair(i,j));
				//bfs���� //bfs�ȿ����� ���Ǽ� input�������
				int num_of_house = 0;
				while (!Q.empty()) {
					num_of_house++;
					int a = Q.front().first;
					int b = Q.front().second;

					Q.pop();

					//��,�Ʒ�,��,�� �߿��� ������ ã��

					//��
					if (v1[a-1][b] == 1 && visited[a - 1][b] == 0) {
						visited[a - 1][b] = num_of_group;
						Q.push(make_pair(a - 1, b));
						
					}
					//�Ʒ�
					if (v1[a+1][b] == 1 && visited[a + 1][b] == 0) {
						visited[a + 1][b] = num_of_group;
						Q.push(make_pair(a + 1, b));

					}
					//��
					if (v1[a][b - 1] == 1 && visited[a][b - 1] == 0) {
						visited[a][b - 1] = num_of_group;
						Q.push(make_pair(a, b - 1));

					}
					//��
					if (v1[a][b+1] == 1 && visited[a][b + 1] == 0) {
						visited[a][b + 1] = num_of_group;
						Q.push(make_pair(a, b + 1));

					}
				}
				vHouse.push_back(num_of_house);
				
			
			}
		}
	}

	cout << num_of_group << "\n";
	sort(vHouse.begin(), vHouse.end());
	for (int i = 0; i < vHouse.size(); i++) {
		cout << vHouse[i] << "\n";
	}
	return 0;
}