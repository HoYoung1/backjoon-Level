#include <stdio.h>
#include <string.h>

int minparent = -1;
int maxparent = -1;
int main() {
	char parenthesis[31];
	scanf("%s", parenthesis);

	int sum = 0;
	int minchk = 1;
	int maxchk = 1;
	int errorflag = 0;
	int len = strlen(parenthesis);
	for (int i = 0; i < len; i++) {
		if (parenthesis[i] == '(') {
			minparent++;
		}
		else if (parenthesis[i] == ')') {
			if (minparent == -1) {
				errorflag = 1;
				break;
			}
			minparent--;
			
			/*if ((parenthesis[i + 1] == '[' || parenthesis[i + 1] == '(')) {
				chk = chk * 2;
			}*/
			minchk = minchk * 2;
			if (minparent == -1 && maxparent == -1) {
				sum = sum + minchk;
				minchk = 1;
			}

		}
		else if (parenthesis[i] == '[') {
			maxparent++;
		}
		else if (parenthesis[i] == ']') {
			if (maxparent == -1) {
				errorflag = 1;
				break;
			}
			maxparent--;

			/*if ((parenthesis[i + 1] == '[' || parenthesis[i + 1] == '(')) {
				chk = chk * 3;
			}*/
			maxchk = maxchk * 3;
			if (minparent == -1 && maxparent == -1) {
				sum = sum + maxchk;
				maxchk = 1;
			}
		}
	}
	

}