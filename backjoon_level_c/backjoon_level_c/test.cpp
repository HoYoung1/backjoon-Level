#include <iostream>
#include <queue>
using namespace std;

int m, n;
int arr[1002][1002];
bool visited[1002][1002];
queue<pair<int, int>> q;
int check[4][2] = { { 0,-1 },{ 0,1 },{ -1,0 },{ 1,0 } };
int day = -1;
int num;		//q�� ���� pushȽ��, �� �Ϸ翡 ������ ������ �ִ� �丶�� ����
int popnum = 0;		//popȽ��, �� num�� ������ �Ϸ翡 ������ �ִ� �丶�䰹���� ����.

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> m >> n;
	//arr�� visited �迭�� �ʱ�ȭ �Ѵ�.
	for (int i = 0; i <= n + 1; i++)
	{
		for (int j = 0; j <= m + 1; j++)
		{
			arr[i][j] = -1;
			visited[i][j] = false;
		}
	}

	//�丶�� ���¸� �Է¹޴´�.
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cin >> arr[i][j];
		}
	}

	//0������ ���� �丶�� ��ǥ�� q�� ����
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
	num = q.size();		//0������ q�� ����ִ� ��ǥ ���� num

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