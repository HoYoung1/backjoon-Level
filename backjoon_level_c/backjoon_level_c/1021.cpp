#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <deque>
#include <queue>
using namespace std;

int main() {

	deque<int> dq;
	queue<int> vFind;
	
	int N; //ť�� ũ�� N, N�� 50���� �۰ų� ���� �ڿ���
	int M; // M�� N���� �۰ų� ���� �ڿ���
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		dq.push_back(i + 1);
	}

	for (int i = 0; i < M; i++) {
		int temp;
		cin >> temp;
		vFind.push(temp);
	}


	int total_cnt = 0;
	while (!vFind.empty()) {

		deque<int> dqtemp = dq;
		queue<int> vFindTemp = vFind;
		int leftcnt = 0;
		while (dqtemp.front() != vFindTemp.front()) {
			int val = dqtemp.front();
			dqtemp.pop_front();
			dqtemp.push_back(val);
			++leftcnt;
		}

		dqtemp = dq;
		vFindTemp = vFind;
		int rightcnt = 0;
		while (dqtemp.front() != vFindTemp.front()) {
			int val = dqtemp.back();
			dqtemp.pop_back();
			dqtemp.push_front(val);
			++rightcnt;
		}

		
		if (rightcnt > leftcnt) {
			//�������� �������ؾ���
			total_cnt += leftcnt;
			while (dq.front() != vFind.front()) {
				int val = dq.front();
				dq.pop_front();
				dq.push_back(val);
			}
			
		}
		else {
			total_cnt += rightcnt;
			while (dq.front() != vFind.front()) {
				int val = dq.back();
				dq.pop_back();
				dq.push_front(val);
			}
		}
		dq.pop_front();
		vFind.pop();
	}

	cout << total_cnt << endl;


	

	return 0;
}

