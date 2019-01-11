#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<vector<bool>> v1;
vector<int> vdp1;
int memo(int n);
int N;
int main() {
	v1.assign(10001, vector<bool>(10001, false));
	vdp1.assign(10001,0);
	int M;

	cin >> N >> M;

	for (int i = 1; i <= M; i++) {
		int a, b;
		cin >> a >> b;
		v1[a][b] = true;
	}

	for (int i = 1; i <= N; i++) {
		memo(i);
	}


	
	int max_num = *max_element(vdp1.begin(),vdp1.end());

	
	for (int i = 1; i <= N; i++) {
		if (vdp1[i] == max_num) {
			cout << i << ' ';
		}
	}
	return 0;
}

int memo(int n) {
	if (vdp1[n] > 0) {
		//이미계산됬으니 return;
		return vdp1[n];
	}
	int sum = 1;
	for (int i = 1; i <= N; i++) {
		if (v1[i][n] == true) {
			sum = sum + memo(i);
		}
	}
	vdp1[n] = sum;
	return vdp1[n];
}