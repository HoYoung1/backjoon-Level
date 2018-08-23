#include <stdio.h>
#include <string.h>

int main() {
	int alpha[26];

	int i;
	for (i = 0; i < 26; i++) {
		alpha[i] = -1;
	}

	char word[101];

	scanf("%s", word);
	int cnt;
	for (i = 0; i < strlen(word); i++) {
		cnt = word[i] - 'a';
		
		if (alpha[cnt] > -1 ) {
			continue;
		}
		else {
			alpha[cnt] = i;
		}
	}

	for (i = 0; i < 26; i++) {
		printf("%d ", alpha[i]);
	}

	return 0;


}