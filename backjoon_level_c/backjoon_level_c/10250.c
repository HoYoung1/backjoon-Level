#include <stdio.h>

int main() {
	int testcase;
	scanf("%d", &testcase);

	int i;
	int h, w, n;
	for (i = 0; i < testcase; i++) {
		scanf("%d %d %d", &h, &w, &n);

		int a, b=0, c=1;
		//n을 10이라고했으면 10번만큼 반복문이돌면서 체크
		for (a = 0; a < n; a++) {
			
			b = b + 1;
			if (b > h) {
				b = 1, c++;
			}
			
			
		}
		if(c<10)
			printf("%d0%d\n", b, c);
		else
			printf("%d%d\n", b, c);
	}
	
	return 0;


}