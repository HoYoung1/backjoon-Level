#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> v1;

int combi_memo(int n, int k) {
	//nCk = n-1Ck-1+n-1Ck

	
	if (v1[n][k] != -1) {
		return v1[n][k];
	}

	if (n == 0) {
		v1[n][k] = 1;
		return v1[n][k];
	}
	else if (k == 0) {
		v1[n][k] = 1;
		return v1[n][k];
	}
	else if (n == k) {
		v1[n][k] = 1;
		return v1[n][k];
	}
	v1[n][k] = combi_memo(n - 1, k - 1) + combi_memo(n - 1, k)%10007;
	return v1[n][k];
}

int main() {
	v1.assign(1005, vector<int>(1005,-1));

	int N, K;

	cin >> N >> K;
	cout << combi_memo(N, K)%10007;

	return 0;
}