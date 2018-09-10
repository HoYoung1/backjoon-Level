#include <stdio.h>

int stack[10000];
int topp = -1;
int main() {
	int input;

	scanf("%d", &input);

	for (int i = 0; i < input; i++) {
		char cmd[6];

		scanf("%s", cmd);
		if (strcmp(cmd, "push") == 0) {
			int num;
			scanf("%d",&num);
			push(num);
		}
		else if (strcmp(cmd, "pop")==0) {
			printf("%d\n", pop());
		}
		else if (strcmp(cmd, "size")==0) {
			printf("%d\n", size());
		}
		else if (strcmp(cmd, "empty")==0) {
			printf("%d\n", empty());
		}
		else if (strcmp(cmd, "top")==0) {
			printf("%d\n", top());
		}
	}
}

int push(int n) {
	stack[++topp] = n;
}

int pop() {
	if (topp > -1) {
		return stack[topp--];
	}
	else {
		return -1;
	}
}

int size() {
	return topp + 1;
}

int empty() {
	if (topp == -1) {
		return 1;
	}
	else
		return 0;
}

int top() {
	if (topp == -1) {
		return -1;
	}
	return stack[topp];
}