#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <limits.h>

using namespace std;

int dp[20001];
int main() {

	int N, M, K;

	cin >> N >> M >> K;

	vector<int> oranges;
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		oranges.push_back(temp);
	}

	for (int i = 0; i < 20001; i++) {
		dp[i] = INT_MAX;
	}
	dp[0] = 0;

	for (int i = 1; i < N+1; i++) {
		for (int j = i-M; j < i; j++) {
			if (j < 0) {
				continue;
			}

			//init
			int max_value = INT_MIN; 
			int min_value = INT_MAX;

			for (int k = j; k < i; k++){
				max_value = max(max_value, oranges[k]);
				min_value = min(min_value, oranges[k]);
			}
			// cout << "max_value : " << max_value << endl;
			// cout << "min_value : " << min_value << endl;

			// cout <<"dp i :" << dp[i] << endl;
			// cout <<"dp j :" << dp[j] << endl;
			
			int value = (max_value - min_value) * (i-j) + K;
			// cout << "valiue : " << value << endl;;
			dp[i] = min(dp[i], dp[j] + (max_value - min_value) * (i-j) + K);
		}
	}

	// for (int i = 0; i < N+1; i++){
	// 	cout << dp[i] << endl;	
	// }
	cout << dp[N];
}