#include <stdio.h>

int count[10001];
int main() {
	int input;

	
	scanf("%d", &input);

	int num;

	for (int i = 0; i < input; i++) {
		scanf("%d", &num);
		count[num - 1]++;
	}

	int k = 0;
	int i = 0;
	while (1) {
		if (k == input) {
			//다 출력했다는 뜻
			break;
		}
		
		while (count[i]--) {
			printf("%d\n", i+1);
			k++;
		}
		i++;
	}

	return 0;


}