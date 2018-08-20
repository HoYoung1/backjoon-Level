#include <stdio.h>
#include <string.h>

int main() {
	char sentence[1000000];

	scanf("%[^\n]s", sentence);
	//printf("%d", strlen(sentence));
	int i,cnt = 0 ;
	for (i = 0; i < strlen(sentence); i++) {
		if (sentence[i] == ' ') {
			cnt++;
		}
	}
	if (sentence[0] == ' ') {
		cnt--;
	}
	if (sentence[strlen(sentence)-1] == ' ') {
		cnt--;
	}
	//else if(sentence[strlen(sentence)])
	printf("%d", cnt+1);

	return 0;
}