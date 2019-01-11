#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {

	int N, M;
	cin >> N >> M;//M�� N�� 8���� ũ�ų� ����, 50���� �۰ų� ���� �ڿ����̴�. 
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

	//ü�������
	for (int i = 0; i <= N - 8; i++) {
		for (int j = 0; j <= M - 8; j++) {
			
			//���� ��
			int cnt = 0;
			for (int k = 0; k < 8; k++) {
				for (int l = 0; l < 8; l++) {
					if (board[i + k][j + l] != WstartBoard[k][l]) {
						//�ٸ��ٸ� cnt++
						cnt++;
					}
				}
			}
			minChg = min(minChg, cnt);
		}
	}

	//ü�������
	for (int i = 0; i <= N - 8; i++) {
		for (int j = 0; j <= M - 8; j++) {

			//���� ��
			int cnt = 0;
			for (int k = 0; k < 8; k++) {
				for (int l = 0; l < 8; l++) {
					if (board[i + k][j + l] != BstartBoard[k][l]) {
						//�ٸ��ٸ� cnt++
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