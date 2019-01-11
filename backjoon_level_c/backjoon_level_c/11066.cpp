#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int K[500];

int main() {

	int T;
	scanf("%d", &T);

	vector<int> v1;
	for (int i = 0; i < T; i++) {
		scanf("%d", &K[i]);
		v1.push_back(K[i]);
	}

	sort(v1.begin(), v1.end());

	for (int i = 0; i < v1.size(); i++) {
		cout << v1[i] << ' ';
	}
	return 0;
}