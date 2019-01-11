#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int a[9];
int main() {
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &a[i]);
		sum = sum + a[i];
	}

	vector<int> v1;
	for (int i = 0; i < 8; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (sum - a[i] - a[j] == 100) {
				for (int k = 0; k < 9; k++) {
					if (k == i || k == j) {
						continue;
					}
					else {
						v1.push_back(a[k]);
					}
				}
				break;
			}
		}
	}

	sort(v1.begin(), v1.end());

	for (int i = 0; i < v1.size(); i++) {
		cout << v1[i] << "\n";
	}

	return 0;

}