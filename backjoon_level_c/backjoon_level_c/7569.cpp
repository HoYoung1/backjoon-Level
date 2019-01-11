#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <queue>
using namespace std;

//3차원 벡터를 선언해야한다.
//int tomatoes[102][102][102];




vector<vector<vector<int>>> tomatoes;
queue<pair<int, pair<int, pair<int,int>>>> Q; //높이 , 가로, 세로 , 며칠째익은 토마토인지 1이면 1일째 익은 토마토

int main() {
	tomatoes.assign(102, vector<vector<int>>(102,vector<int>(102,-2)));

	int M, N, H;

	cin >> M >> N >> H;
	
	int count_0 = 0;
	int count_change = 0;
	bool chkAll1 = true;
	int day_of_tomato = 0;
	//-2로 초기화 되어있습니다.
	//M = 2~100
	//N = 2~100
	//H = 1~100


	//1은 익은토마토 
	//0은 익지않은토마토
	//-1은 토마토가 들어있지 않은 칸 


	//i는 높이 j,k가 가로 세로
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= N; j++) {
			for (int k = 1; k <= M; k++) {				
				scanf("%d", &tomatoes[i][j][k]);
				

				//만약 하나라도 1이 아닌것이 잇으면 false 전부다 1이라면 true 반환.
				if (chkAll1 == true && tomatoes[i][j][k]!=1) {
					chkAll1 = false;
				}


				if (tomatoes[i][j][k] == 0) {
					count_0++;
				}
				
				if (tomatoes[i][j][k] == 1) {
					//큐에 넣어야합니다.
					Q.push(make_pair(i,make_pair(j,make_pair(k, day_of_tomato)))); //to do 큐에 잘들어갓는지 확인.(문법)
				}


				//출력확인
				// cout << tomatoes[i][j][k] << ' ';
			}
			
		}
	
	}


	//BFS
	while (!Q.empty()) {
		int a=Q.front().first; //높이
		int b= Q.front().second.first;//가로
		int c= Q.front().second.second.first;//세로
		int day = (Q.front().second.second.second); //day = day_of_tomato + 1
		if (day > day_of_tomato)
			day_of_tomato = day; //최종 출력 값인 최소 일자를 나타냄

		Q.pop();

		//위, 아래, 왼쪽, 오른쪽, 앞, 뒤 : 여섯 방향 변환가능

		//위
		if (tomatoes[a+1][b][c] == 0) {
			//1로 바꾸고 큐에푸시
			tomatoes[a + 1][b][c] = 1;
			Q.push(make_pair(a + 1, make_pair(b, make_pair(c,day+1))));
			count_change++;
		}

		//아래
		if (tomatoes[a-1][b][c] == 0) {
			//1로 바꾸고 큐에푸시
			tomatoes[a - 1][b][c] = 1;
			Q.push(make_pair(a - 1, make_pair(b, make_pair(c, day + 1))));
			count_change++;
		}

		//왼쪾
		if (tomatoes[a][b][c - 1] == 0) {
			//1로 바꾸고 큐에푸시
			tomatoes[a][b][c - 1] = 1;
			Q.push(make_pair(a, make_pair(b, make_pair(c - 1, day + 1))));
			count_change++;
		}
		


		//오른쪽
		if (tomatoes[a][b][c + 1] == 0) {
			//1로 바꾸고 큐에푸시
			tomatoes[a][b][c + 1] = 1;
			Q.push(make_pair(a, make_pair(b, make_pair(c+1, day + 1))));
			count_change++;
		}

		//앞
		if (tomatoes[a][b - 1][c] == 0) {
			//1로 바꾸고 큐에푸시
			tomatoes[a][b-1][c] = 1;
			Q.push(make_pair(a , make_pair(b-1, make_pair(c, day + 1))));
			count_change++;
		}

		//뒤
		if (tomatoes[a][b + 1][c] == 0) {
			//1로 바꾸고 큐에푸시
			tomatoes[a][b + 1][c] = 1;
			Q.push(make_pair(a, make_pair(b + 1, make_pair(c, day + 1))));
			count_change++;
		}
	}

	


	//저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력(입력을 받았는데 전부다 1이라면 0출력)
	//토마토가 모두 익지는 못하는 상황이면 -1 (0입력받은 갯수와 변환시킨 갯수가 같지않다면 -1출력하면될듯)

	//to do 위 두문장에대한 출력처리
	if (chkAll1 == true)
		cout << "0";
	else if (count_0 != count_change) {
		cout << "-1";
	}
	else {
		cout << day_of_tomato;
	}
	return 0;
}