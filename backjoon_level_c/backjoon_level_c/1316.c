#include <stdio.h>

int main() {
	char words[101];

	int testcase;

	scanf("%d", &testcase);

	
	
	int i,j,k;
	int groupcnt=0;
	int flag;
	for (i = 0; i<testcase; i++) {
		scanf("%s", words);
		flag = 1;
		char before = '0';
		char beforearr[101] = {0,};
		int cnt = 0;
		for (j = 0; words[j] != '\0'; j++) {
		
			if (words[j]!=before) {
				
				for (k = 0; k < cnt; k++) {
					if (beforearr[k] == words[j]) {
						//�� ���� �׷� �ܾ �ƴ�.
						flag = 0;
					}
				}
				beforearr[cnt] = words[j];
				before = words[j];
				cnt++;

			}

			
		}
		if (flag == 1) {
			//�׷�ܾ��Դϴ�.
			groupcnt++;
		}
	}
	printf("%d", groupcnt);

	return 0;
}