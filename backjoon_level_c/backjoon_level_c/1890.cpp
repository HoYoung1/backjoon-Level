//#include <iostream>
//#include <cstdio>
//#include <vector>
//
//using namespace std;
//vector<vector<int>> v1;
//void DFS(int x, int y);
//int count_way = 0;
//int N;
//int main() {
//
//	
//	
//	cin >> N;
//	v1.assign(102, vector<int>(102, -1));
//
//	for (int i = 1; i <= N; i++) {
//		for (int j = 1; j <= N; j++) {
//			scanf("%d", &v1[i][j]);
//		}
//	}
//
//
//
//	DFS(1, 1);
//	cout << count_way;
//	return 0;
//}
//
//void DFS(int x, int y) {
//	
//
//	if (v1[x][y] == 0) {
//		//������ ����
//		count_way++;
//		return;
//	}
//	//�Ʒ�����, �״��� ������
//	int value = v1[x][y];
//	if (value + x <= N) {
//		DFS(value + x, y);
//	}
//	if (value + y <= N) {
//		DFS(x, value+y);
//	}
//}


//������ �Ϲ����� DFS �ð��ʰ��ڵ���.

//�ؿ��� dp�� �����Ұ���. �޸������̼ǻ��.

#include <iostream>

#include <vector>
#include <cstdio>

using namespace std;
vector<vector<long long>> vdp1;
vector<vector<int>> v1;

int count_way = 0;
int N;

long long memo(int x, int y);

int main() {
	vdp1.assign(102, vector<long long>(102, 0));
	v1.assign(102, vector<int>(102, -1));
	cin >> N;
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			scanf("%d", &v1[i][j]);
		}
	}

	cout << memo(N, N);
	
	return 0;
}

long long memo(int x, int y) {
	long long sum = 0;

	if ((x == 1 && y == 1)) {
		return 1;
	}

	if (vdp1[x][y] > 0  ) {
		//���������� �ִ�
		return vdp1[x][y];
	}
	
	//x��� y�� Ȯ���ϸ� �����Ҽ��ִ� ����Ʈ�� ã��������
	int i;

	//���� ���� �˻��Ѵ�
	i = y - 1;
	while (i > 0) {
		if (i + v1[x][i] == y)
			sum = sum + memo(x, i);
		i--;
	}

	//���˻�



	
	i = x - 1;
	while (i > 0) {
		if (i + v1[i][y] == x)
			sum = sum + memo(i, y);
		i--;
	}
	
	vdp1[x][y] = sum;
	
	
	

	return vdp1[x][y];
}