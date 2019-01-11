#include <iostream>

using namespace std;

int fac(int a) {
	if (a == 0 || a==1)
		return 1;
	return a * fac(a - 1);
}
int combination(int n ,int k) {
	return fac(n) / (fac(k)*fac(n-k));
}
int main() {
	int N, K;

	cin >> N >> K;

	cout << combination(N, K);
	return 0;
}