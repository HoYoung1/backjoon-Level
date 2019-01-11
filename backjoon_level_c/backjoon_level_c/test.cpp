#include <iostream>
#include <queue>
using namespace std;

int m, n;
int arr[1002][1002];
bool visited[1002][1002];
queue<pair<int, int>> q;
int check[4][2] = { { 0,-1 },{ 0,1 },{ -1,0 },{ 1,0 } };
int day = -1;
int num;		//q에 들어가는 push횟수, 즉 하루에 주위를 익힐수 있는 토마토 갯수
int popnum = 0;		//pop횟수, 즉 num과 같으면 하루에 익힐수 있는 토마토갯수는 없다.

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> m >> n;
	//arr와 visited 배열을 초기화 한다.
	for (int i = 0; i <= n + 1; i++)
	{
		for (int j = 0; j <= m + 1; j++)
		{
			arr[i][j] = -1;
			visited[i][j] = false;
		}
	}

	//토마토 상태를 입력받는다.
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cin >> arr[i][j];
		}
	}

	//0일차에 익은 토마토 좌표를 q에 삽입
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			if (!visited[i][j] && (arr[i][j] == 1))
			{
				q.push(make_pair(i, j));
				visited[i][j] = true;
			}
		}
	}
	num = q.size();		//0일차에 q에 들어있는 좌표 갯수 num

	while (!q.empty())
	{
		int first = q.front().first;
		int second = q.front().second;
		q.pop();
		popnum++;
		//arr[first][second] = 1;

		for (int i = 0; i < 4; i++)
		{
			int n_first = first + check[i][0];
			int n_second = second + check[i][1];

			if ((arr[n_first][n_second] == 0) && !visited[n_first][n_second])
			{
				q.push(make_pair(n_first, n_second));
				arr[n_first][n_second] = 1;
				visited[n_first][n_second] == true;
			}
		}
		if (num == popnum)
		{
			num = q.size();
			popnum = 0;
			day++;
		}
	}
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			if (arr[i][j] == 0)
				day = -1;
		}
	}
	cout << day << "\n";
	return 0;
}