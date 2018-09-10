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
			//countM���� ���̰�
			//ť���� �ϴ� ���� countM�� 0�̸� ���,�ƴϸ� �ڷ� �ְڽ��ϴ�.
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
	//0�� ��ȯ�Ѵٸ� ť�� ��������� �ǹ��մϴ�.
	if (isEmpty()) {
		return 0;
	}
	int deNum = queue[front];
	front = (front + 1) % MAXSIZE;
	return deNum;
}
int isEmpty() {
	//1�� ��ȯ�Ѵٸ� ��������� �ǹ��մϴ�.
	if (front == rear) {
		return 1;
	}
	else
		return 0;
}