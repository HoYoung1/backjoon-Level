#include<cstdio>
const int MAX_N = 18;
int N, M, b[MAX_N][MAX_N], ans = 1e9, sel[MAX_N], rsum[MAX_N];
void back(int p){
	if(p == N){
		int tmp = 0, csum, i, j, valid = 1;
		for(i=0;i<N;i++) { // row sum 을 구함
			tmp += sel[i];
			rsum[i] = 0;
			for(j=0;j<M;j++) {
				if(sel[i]) b[i][j] = -b[i][j];
				rsum[i] += b[i][j];
			}
		}
		for(j=0;j<M;j++) {
			csum = 0;
			for(i=0;i<N;i++)
				csum += b[i][j];
			if(csum <= 0){
				valid &= csum != 0;
				for(i=0;i<N;i++)
					rsum[i] -= 2 * b[i][j];
				tmp++;
			}
		}
		for(i=0;i<N;i++) {
			valid &= rsum[i] > 0;
			if(sel[i]) for(j=0;j<M;j++)
				b[i][j] = -b[i][j];
		}
		if(valid)
			ans = ans < tmp ? ans : tmp;
		return;
	}
	back(p + 1);

	sel[p] = 1;
	back(p+1);
	sel[p] = 0;
}
int main() {
	int i, j;
	// scanf("%d%d",&N,&M);
	// for(i=0;i<N;i++) for(j=0;j<M;j++)
	// 	scanf("%d",&b[i][j]);
	N = 2;
	M = 2;

	b[0][0] = -26;
	b[0][1] = 2;
	b[1][0] = 2;
	b[1][1] = 1;

	back(0);
	printf("%d", ans == 1e9 ? -1 : ans);
	return 0;
}