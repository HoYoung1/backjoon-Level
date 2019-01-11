#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <deque>
using namespace std;

int isEmpty(deque<int> dq);
int main() {
	ios_base::sync_with_stdio(false);
	int N;
	cin >> N;

	deque<int> dq;
	for (int i = 0; i < N; i++) {
		string order;
		cin >> order;

		if (order == "push_back") {
			int data;
			cin >> data;
			dq.push_back(data);
		}
		else if (order == "push_front") {
			int data;
			cin >> data;
			dq.push_front(data);
		}
		else if (order == "front") {
			if (!dq.empty()) {
				cout << dq.front() << endl;
			}
			else {
				cout << "-1" << endl;
			}
			
		}
		else if (order == "back") {
			if (!dq.empty()) {
				cout << dq.back() << endl;
			}
			else {
				cout << "-1" << endl;
			}
			
		}
		else if (order == "size") {
			cout << dq.size() << endl;
		}
		else if (order == "empty") {
			cout << isEmpty(dq) << endl;
		}
		else if (order == "pop_back") {
			if (!dq.empty()) {
				cout << dq.back() << endl;
				dq.pop_back();
			}
			else {
				cout << "-1" << endl;
			}
			
		}
		else if (order == "pop_front") {
			if (!dq.empty()) {
				cout << dq.front() << endl;
				dq.pop_front();
			}
			else {
				cout << "-1" << endl;
			}
			
		}
	}

	return 0;
}

int isEmpty(deque<int> dq) {
	
	//비었다면 1 값이 있으면 0
	if (dq.empty() == true) {
		return 1;
	}
	return 0;
}