#include <stdio.h>

#define MAXSIZE 5001
int queue[MAXSIZE];
int rear = 0, front = 0;

void enqueue(int num);
int dequeue();
int isEmpty();

int main() {
	
	int N, M;
	scanf("%d %d",&N,&M);
	
	for (int i = 0; i < N; i++) {
		enqueue(i + 1);
	}
	int countM = M;
	printf("<");
	while (1) {
		if (isEmpty()) {
			break;
		}
		else {
			//countM먼저 줄이고
			//큐에서 일단 빼고 countM이 0이면 출력,아니면 뒤로 넣겠습니다.
			countM--;
			int temp = dequeue();
			if (countM == 0) {
				printf("%d", temp);
				if (isEmpty()) {
					printf(">");
					break;
				}
				else {
					printf(", ");
				}
				countM = M;
			}
			else {
				enqueue(temp);
			}
			
		}
	}
	

	return 0;
}

void enqueue(int num) {

	queue[rear] = num;
	rear = (rear + 1)% MAXSIZE;
}
int dequeue() {
	//0을 반환한다면 큐가 비어있음을 의미합니다.
	if (isEmpty()) {
		return 0;
	}
	int deNum = queue[front];
	front = (front + 1) % MAXSIZE;
	return deNum;
}
int isEmpty() {
	//1을 반환한다면 비어있음을 의미합니다.
	if (front == rear) {
		return 1;
	}
	else
		return 0;
}