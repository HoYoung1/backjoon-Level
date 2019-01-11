#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {

	int N, K;
	cin >> N >> K; // 1<=N<=500  , 1<=K<=N
	vector<int> vDolls;
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		vDolls.push_back(temp);
	}

	long double minst = 9876543210;

	for (int j = K; j<= N; j++) { // 3 4 5
		for (int k = 0; k < N; k++) {
			if (k + j > N) break; // 이미다했음 묶는거까지

			long double sum = 0;
			for (int i = k; i < k+j; i++) {
				sum = sum + vDolls[i];
			}
			long double m =sum / j;

			long double powSum = 0;
			for (int i = k; i < k+j; i++) {
				powSum += pow(vDolls[i] - m, 2);
			}
			minst = min(sqrt(powSum / j), minst); //st = 분산
		}
		
		
	}
	cout << fixed;
	cout.precision(11);
	cout << minst;
	//printf("%Lf", sqrt(minst));

	return 0;
}