#include <iostream>
#include <string>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	
	while (true) {
		string s;
		getline(cin, s);

		if (s == "END") {
			break;
		}

		for (int i = s.size() - 1; i >= 0; i--) {
			cout << s[i];
		}
		cout << endl;
	}
	
	
	

	

	return 0;
}