#include <stdio.h>

int main() {
	char words[101];

	scanf("%s", words);

	int i;
	int cnt = 0;
	for (i = 0; words[i] != '\0'; i++) {
		if (words[i] == 'c')  {
			if (words[i + 1] == '=' || words[i + 1] == '-') {
				i++;
			}
		}
		else if (words[i] == 'd') {
			if (words[i + 1] == 'z') {
				if (words[i + 2] == '=') {
					i = i + 2;
				}
			}
			else if (words[i+1]=='-') {
				i++;
			}
		}
		else if (words[i] == 'l' && words[i+1] == 'j') {
			i++;
		}
		else if (words[i] == 'n' && words[i + 1] == 'j') {
			i++;
		}
		else if (words[i] == 's' && words[i + 1] == '=') {
			i++;
		}
		else if (words[i] == 'z' && words[i + 1] == '=') {
			i++;
		}
		cnt++;
	}
	printf("%d", cnt);
	return 0;
}