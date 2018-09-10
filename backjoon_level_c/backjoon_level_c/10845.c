#include <stdio.h>

#define MAXSIZE 10000
int queue[MAXSIZE];
int rear = 0, front = 0;

int main() {
	int input;

	scanf("%d", &input);

	for (int i = 0; i < input; i++) {
		char cmd[6];
		scanf("%s", cmd);

		if (strcmp(cmd, "push") == 0) {
			int num;
			scanf("%d", &num);

			push(num);
		}
		else if (strcmp(cmd, "front") == 0) {
			printf("%d\n", frontPrint());
		}
		else if (strcmp(cmd, "back") == 0) {
			printf("%d\n", backPrint());
		}
		else if (strcmp(cmd, "size") == 0) {
			printf("%d\n", sizePrint());
		}
		else if (strcmp(cmd, "empty") == 0) {
			printf("%d\n", isEmpty());
		}
		else if (strcmp(cmd, "pop") == 0) {
			printf("%d\n", pop());
		}
	}
}

int push(int X) {
	//제일 먼저 꽉찼는지 검사

	if ((rear + 1) % 10000 == front) {
		//따로 처리 없음.
	}
	queue[rear] = X;
	rear = (rear + 1) % MAXSIZE;

}

int pop() {
	//제일 먼저 비어있는지 검사
	if (front == rear) {
		return -1;
	}
	int i = queue[front];
	front = (front + 1) % MAXSIZE;

	return i;
}

int sizePrint() {
	if (rear < front) {
		return rear + MAXSIZE - front;
	}
	return rear - front;
}

int isEmpty() {
	if (front == rear) {
		return 1;
	}
	else
		return 0;
}

int frontPrint() {
	if (front == rear) {
		return -1;
	}
	else
		return queue[front];
}

int backPrint() {
	if (front == rear) {
		return -1;
	}
	else
		return queue[rear-1];
}