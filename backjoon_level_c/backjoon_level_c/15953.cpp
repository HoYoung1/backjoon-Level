#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
vector<pair<int, int>> p1;
vector<pair<int, int>> p2;
int main() {

	p1.push_back(make_pair(500, 1));
	p1.push_back(make_pair(300, 2));
	p1.push_back(make_pair(200, 3));
	p1.push_back(make_pair(50, 4));
	p1.push_back(make_pair(30, 5));
	p1.push_back(make_pair(10, 6));

	p2.push_back(make_pair(512, 1));
	p2.push_back(make_pair(256, 2));
	p2.push_back(make_pair(128, 4));
	p2.push_back(make_pair(64, 8));
	p2.push_back(make_pair(32, 16));

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int a, b;
		cin >> a >> b;
		int sum = 0;

		for (int j = 0; j <p1.size(); j++) {
			int temp = p1[j].second;
			bool bFlag = false;
			while (temp--) {
				if (--a == 0) {
					sum = sum + p1[j].first;
					bFlag = true;
					break;
				}
				
			}
			if (bFlag) break;
		}

		for (int j = 0; j < p2.size(); j++) {
			int temp = p2[j].second;
			bool bFlag = false;
			while (temp--) {
				if (--b == 0) {
					sum = sum + p2[j].first;
					bFlag = true;
					break;
				}

			}
			if (bFlag) break;
		}
		cout << sum*10000 << endl;
	}
	



	return 0;
}