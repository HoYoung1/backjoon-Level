#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;//M과 N은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
	string board[50];

	for (int i = 0; i < N; i++) {
		cin >> board[i];
	}

	string WstartBoard[8] = {
		"WBWBWBWB",
		"BWBWBWBW",
		"WBWBWBWB",
		"BWBWBWBW",
		"WBWBWBWB",
		"BWBWBWBW",
		"WBWBWBWB",
		"BWBWBWBW"
	};

	string BstartBoard[8] = {
		"BWBWBWBW",
		"WBWBWBWB",
		"BWBWBWBW",
		"WBWBWBWB",
		"BWBWBWBW",
		"WBWBWBWB",
		"BWBWBWBW",
		"WBWBWBWB",
	};
	int minChg = 99999999;

	//체스판찍기
	for (int i = 0; i <= N - 8; i++) {
		for (int j = 0; j <= M - 8; j++) {
			
			//글자 비교
			int cnt = 0;
			for (int k = 0; k < 8; k++) {
				for (int l = 0; l < 8; l++) {
					if (board[i + k][j + l] != WstartBoard[k][l]) {
						//다르다면 cnt++
						cnt++;
					}
				}
			}
			minChg = min(minChg, cnt);
		}
	}

	//체스판찍기
	for (int i = 0; i <= N - 8; i++) {
		for (int j = 0; j <= M - 8; j++) {

			//글자 비교
			int cnt = 0;
			for (int k = 0; k < 8; k++) {
				for (int l = 0; l < 8; l++) {
					if (board[i + k][j + l] != BstartBoard[k][l]) {
						//다르다면 cnt++
						cnt++;
					}
				}
			}
			minChg = min(minChg, cnt);
		}
	}



	cout << minChg;

	return 0;
}