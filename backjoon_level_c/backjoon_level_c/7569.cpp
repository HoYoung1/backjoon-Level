#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <queue>
using namespace std;

//3���� ���͸� �����ؾ��Ѵ�.
//int tomatoes[102][102][102];




vector<vector<vector<int>>> tomatoes;
queue<pair<int, pair<int, pair<int,int>>>> Q; //���� , ����, ���� , ��ĥ°���� �丶������ 1�̸� 1��° ���� �丶��

int main() {
	tomatoes.assign(102, vector<vector<int>>(102,vector<int>(102,-2)));

	int M, N, H;

	cin >> M >> N >> H;
	
	int count_0 = 0;
	int count_change = 0;
	bool chkAll1 = true;
	int day_of_tomato = 0;
	//-2�� �ʱ�ȭ �Ǿ��ֽ��ϴ�.
	//M = 2~100
	//N = 2~100
	//H = 1~100


	//1�� �����丶�� 
	//0�� ���������丶��
	//-1�� �丶�䰡 ������� ���� ĭ 


	//i�� ���� j,k�� ���� ����
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= N; j++) {
			for (int k = 1; k <= M; k++) {				
				scanf("%d", &tomatoes[i][j][k]);
				

				//���� �ϳ��� 1�� �ƴѰ��� ������ false ���δ� 1�̶�� true ��ȯ.
				if (chkAll1 == true && tomatoes[i][j][k]!=1) {
					chkAll1 = false;
				}


				if (tomatoes[i][j][k] == 0) {
					count_0++;
				}
				
				if (tomatoes[i][j][k] == 1) {
					//ť�� �־���մϴ�.
					Q.push(make_pair(i,make_pair(j,make_pair(k, day_of_tomato)))); //to do ť�� �ߵ����� Ȯ��.(����)
				}


				//���Ȯ��
				// cout << tomatoes[i][j][k] << ' ';
			}
			
		}
	
	}


	//BFS
	while (!Q.empty()) {
		int a=Q.front().first; //����
		int b= Q.front().second.first;//����
		int c= Q.front().second.second.first;//����
		int day = (Q.front().second.second.second); //day = day_of_tomato + 1
		if (day > day_of_tomato)
			day_of_tomato = day; //���� ��� ���� �ּ� ���ڸ� ��Ÿ��

		Q.pop();

		//��, �Ʒ�, ����, ������, ��, �� : ���� ���� ��ȯ����

		//��
		if (tomatoes[a+1][b][c] == 0) {
			//1�� �ٲٰ� ť��Ǫ��
			tomatoes[a + 1][b][c] = 1;
			Q.push(make_pair(a + 1, make_pair(b, make_pair(c,day+1))));
			count_change++;
		}

		//�Ʒ�
		if (tomatoes[a-1][b][c] == 0) {
			//1�� �ٲٰ� ť��Ǫ��
			tomatoes[a - 1][b][c] = 1;
			Q.push(make_pair(a - 1, make_pair(b, make_pair(c, day + 1))));
			count_change++;
		}

		//�ަU
		if (tomatoes[a][b][c - 1] == 0) {
			//1�� �ٲٰ� ť��Ǫ��
			tomatoes[a][b][c - 1] = 1;
			Q.push(make_pair(a, make_pair(b, make_pair(c - 1, day + 1))));
			count_change++;
		}
		


		//������
		if (tomatoes[a][b][c + 1] == 0) {
			//1�� �ٲٰ� ť��Ǫ��
			tomatoes[a][b][c + 1] = 1;
			Q.push(make_pair(a, make_pair(b, make_pair(c+1, day + 1))));
			count_change++;
		}

		//��
		if (tomatoes[a][b - 1][c] == 0) {
			//1�� �ٲٰ� ť��Ǫ��
			tomatoes[a][b-1][c] = 1;
			Q.push(make_pair(a , make_pair(b-1, make_pair(c, day + 1))));
			count_change++;
		}

		//��
		if (tomatoes[a][b + 1][c] == 0) {
			//1�� �ٲٰ� ť��Ǫ��
			tomatoes[a][b + 1][c] = 1;
			Q.push(make_pair(a, make_pair(b + 1, make_pair(c, day + 1))));
			count_change++;
		}
	}

	


	//����� ������ ��� �丶�䰡 �;��ִ� �����̸� 0�� ���(�Է��� �޾Ҵµ� ���δ� 1�̶�� 0���)
	//�丶�䰡 ��� ������ ���ϴ� ��Ȳ�̸� -1 (0�Է¹��� ������ ��ȯ��Ų ������ �����ʴٸ� -1����ϸ�ɵ�)

	//to do �� �ι��忡���� ���ó��
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