#include <iostream>
#include <string>

using namespace std;

int main() {

	string h;
	cin >> h;

	int sz = h.size();
	for (int i = 0; i < sz; i++) {
		if (isupper(int(h[i])) != 0) {
			cout << h[i];
		}
	}

	return 0;
}