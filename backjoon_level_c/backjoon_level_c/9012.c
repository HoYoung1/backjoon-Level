#include <stdio.h>
#include <string.h>

char VPS[51];

int top = -1;

int main() {
	int T;

	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%s", VPS);

		int flag = 0;
		int len = strlen(VPS);
		top = -1;
		for (int j = 0; j < len; j++) {
			if (VPS[j]=='(') {
				top++;
			}
			else {
				if (top == -1) {
					flag = 1;
					break;
				}
				top--;
			}
			
		}
		if (flag == 1 || top != -1)
			printf("NO\n");
		else
			printf("YES\n");
	}

	return 0;
}