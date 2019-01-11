#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;


int dx[] = { -1,0,1,0 };
int dy[] = { 0,1,0,-1 };

int escapeTime(int w, int h, vector<vector<char>> mapp, queue<pair<int, int>> qFire, queue<pair<int, int>> qEsca) {
	int time = 0;
	while (!qEsca.empty()) {
		++time;

		//���� ���� Ȯ���Ű��
		int qfireSize = qFire.size();
		for (int f = 0; f < qfireSize;f++) {
			int fireX = qFire.front().first;
			int fireY = qFire.front().second;
			qFire.pop();

			//bool bFlag = false; // �ٽ� ť�� ���� ���������� üũ
			for (int i = 0; i < 4; i++) {
				if (mapp[fireX + dx[i]][fireY + dy[i]] == '.' || mapp[fireX + dx[i]][fireY + dy[i]] == '@') {
					//Ȯ�갡��
					mapp[fireX + dx[i]][fireY + dy[i]] = '*';
					qFire.push(make_pair(fireX+dx[i], fireY+dy[i]));
		//			bFlag = true;
				}
			}
		//	if (bFlag)  qFire.push(make_pair(fireX, fireY));
		}

		//Ż���� Ȯ���Ű��
		int qEscaSize = qEsca.size();
		for (int k = 0; k < qEscaSize; k++) {
			int eX = qEsca.front().first;
			int eY = qEsca.front().second;

			qEsca.pop();

			for (int i = 0; i < 4; i++) {
				if (mapp[eX + dx[i]][eY + dy[i]] == 'e') {
					return time; // Ż�ⱸ ã������.
				}
				if (mapp[eX + dx[i]][eY + dy[i]] == '.') {
					//�����̱� ����
					mapp[eX + dx[i]][eY + dy[i]] = '@';
					qEsca.push(make_pair(eX + dx[i], eY + dy[i])); //�̷����ϸ�?
				}
			}
		}
		

	}

	//todo return ;
	return -1;
}
int main() {

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		queue<pair<int, int>> qFire;
		queue<pair<int, int>> qEsca;

		int w, h;
		cin >> w >> h;

		vector<vector<char>> mapp;
		mapp.assign(h + 2, vector<char>(w + 2, 'e'));

		for (int j = 1; j <= h; j++) {
			for (int k = 1; k <= w; k++) {
				char tempc;
				cin >> tempc;
				mapp[j][k] = tempc;
				if (tempc == '*') qFire.push(make_pair(j, k));
				else if (tempc == '@') qEsca.push(make_pair(j, k));
			}
		}//�Է³�

		//for (int j = 1; j <= h; j++) {
		//	for (int k = 1; k <= w; k++) {
		//		cout << mapp[j][k];
		//	}
		//	cout << endl;
		//}//���Ȯ��

		int rtn= escapeTime(w,h,mapp, qFire,qEsca);
		if (rtn == -1) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << rtn << endl;
		}
		
	}

	return 0;
}