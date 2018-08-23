

#include <stdio.h>

int main() {
	char string[1000001];
	
	int alpha[26] = {0, };

	scanf("%s", string);
	int i;
	int max =-1 ;
	int index;
	char ans;
	for (i = 0; i != '\0'; i++) {
		

		if (string[i] < 'a') {
			index = string[i] - 'A';
			alpha[index] += 1;
		}
		else {
			index = string[i] - 'a';
			alpha[index] += 1;
		}

		if (max < alpha[index]) {
			max = alpha[index];
			if (string[i] >= 'a')
				ans = string[i] - 32;
			else {
				ans = string[i];
			}
		}
		else if(max == alpha[index]){
			ans = '?';
		}
	}
	printf("%c", ans);
	

	return 0;

}