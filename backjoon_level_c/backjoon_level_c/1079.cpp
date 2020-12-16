#include <iostream>
using namespace std;

int N, eunjin;
int ans = -1;

int guilt[16];
int R[16][16];
bool visit[16];

// 유죄점수가 가장 높은 idx구하기, 같으면 낮은 idx
int calculate()
{
    int idx = -1;
    int idx_point = -10000;
 
    for (int i = 0; i < N; i++)
    {
        if (guilt[i] > idx_point && !visit[i])
        {
            idx = i;
            idx_point = guilt[i];
        }
    }
    return idx;
}

void dfs(int numPeopleLeft, int nightCount){
    if(nightCount > ans){
        ans = nightCount;
    }

    int idx = -1;
    if(numPeopleLeft % 2 != 0){
        idx = calculate();
        if(idx == eunjin){
            return;
        }
        visit[idx] = true;
        --numPeopleLeft;
    }
    // 밤
    for(int i=0;i<N;i++){
        if(visit[i] == false){
            visit[i] = true;
            --numPeopleLeft;

            for(int j=0;j<N;j++){
                guilt[j] += R[i][j];
            }
            dfs(numPeopleLeft, nightCount + 1);
            for(int j=0;j<N;j++){
                guilt[j] -= R[i][j];
            }
            
            ++numPeopleLeft;
            visit[i] = false;
        }
    }
    // 재귀 끝날때 낮에 죽은사람 다시 살려야함
    if(numPeopleLeft % 2 != 0){
        visit[idx] = false;
        ++numPeopleLeft;
    }
}
int main(){
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> guilt[i];
    
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> R[i][j];
    
    cin >> eunjin;
    visit[eunjin] = true;
    dfs(N, 0);

    cout << ans;

    return 0;
}