#include <string>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> visited;
vector<vector<int>> virus;
queue<int> Q;
int main() {

	visited.assign(101, 0); // 0부터 말고 1부터로 세자
	virus.assign(101, vector<int>(101, -1));

	int virus_computer = 0;
	
	int num_of_computer, num_of_edge;

	cin >> num_of_computer;
	cin >> num_of_edge;
	
	for (int i = 1; i <= num_of_edge; i++) {
		int M, N;
		cin >> M >> N;
		virus[M][N] = 1;
		virus[N][M] = 1;
	}
	
	//1번컴퓨터를 큐에넣는다
	Q.push(1);
	visited[1] = 1;

	while (!Q.empty()) {
		int a = Q.front();

		Q.pop();

		for (int i = 1; i <= num_of_computer; i++) {
			if (virus[a][i] == 1 && visited[i] == 0) {
				visited[i] = 1;
				Q.push(i);
				virus_computer++;
			}
		}
	


	}
	cout << virus_computer;
	return 0;
}