//#include <stdio.h>
//
//int printer[100];
//int queue[101];
//int main() {
//	int input;
//
//	
//	scanf("%d", &input);
//
//	int searchNum;
//	int num;
//	for (int i = 0; i < input; i++) {
//		scanf("%d %d", &num, &searchNum);
//		searchNum++;
//		//searchNum ==2 ��� 2��° ���Ұ� ���°�� ��µǴ��� 
//		//popcnt�� ���° ������ �˷��ٰ��Դϴ�.
//
//		int front = 0, rear = 0;
//		for (int j = 0; j < num; j++) {
//			scanf("%d", &printer[j]);
//
//			queue[rear++] = printer[j];
//		}
//
//
//		while (front<rear) { // ť�ȿ����̵��ִٸ�
//			int flag = 0;
//			int popcnt = 0;
//			int pop = queue[front];
//			front++;
//			for (int k = front; k < rear; k++) {
//				if (queue[k] > pop) {
//					//�ڿ� ������ ū �켱������ �����ְ�����
//					queue[rear] = pop;
//					rear++;
//					flag = 1; // ����� �ƴ�. �ڿ��Ѿ�ٴ°�
//					if (searchNum == 0) {
//						//searchNum�� �ڷΰ��ٴ¼Ҹ��ϱ�
//						if (rear < front) {
//							searchNum = rear+101 - front-1;
//						}
//						else {
//							searchNum = rear - front-1;
//						}
//					}
//					else {
//						searchNum--;
//					}
//					
//					break;
//					//�ٽ� �ǵڿ� �ִ°��� 
//					
//				}
//				else {
//					if (searchNum == 0) {
//						//searchNum�� �ڷΰ��ٴ¼Ҹ��ϱ�
//						if (rear < front) {
//							searchNum = rear + 101 - front - 1;
//						}
//						else {
//							searchNum = rear - front ;
//						}
//					}
//					else {
//						searchNum--;
//					}
//				}
//				
//			}
//			if (flag == 0) {
//				
//				//���� ū���� �տ��־��� �������
//				printf("popcnt �����߽��ϴ�\n");
//				popcnt++;
//			}
//			if (flag == 0 && searchNum == 0) {
//				printf("%d\n", popcnt);
//				break;
//			}
//		}
//		
//		
//		
//
//
//	}
//	return 0;
//}

//#include <stdio.h>
//
//#define MAXSIZE 101
//
//int printer[100];
//int queue[MAXSIZE]; //% �������ʿ�
//
//int main() {
//	int input;
//
//
//	scanf("%d", &input);
//
//	int searchNum;
//	int num;
//	for (int i = 0; i < input; i++) {
//		//�׽�Ʈ ���̽� ������ �ش��ϴ� �ݺ���
//		scanf("%d ", &num );
//		scanf("%d ", &searchNum );
//		//searchNum ==2 ��� 2��° ���Ұ� ���°�� ��µǴ��� 
//		//popcnt�� ���° ������ �˷��ٰ��Դϴ�.
//
//		int front = 0, rear = 0;
//		for (int j = 0; j < num; j++) {
//			scanf("%d", &printer[j]);
//
//			queue[rear] = printer[j];
//			rear = (rear + 1) % MAXSIZE;
//		}
//
//		while (front < rear) {
//			int popcnt = 0; //��°�
//			int temp = queue[front];
//			int flag = 0;
//			int cnt = rear; 
//			for (int k = front; k < cnt; k = (k + 1) % MAXSIZE) {
//				if (queue[k] < queue[k+1]) {
//					//��ū �켱������ ����Ʈ�������Ƿ� �ǵڷγ���
//					queue[rear] = temp;
//					rear = (rear + 1) % MAXSIZE;
//					front = (front + 1) % MAXSIZE;
//
//					//searchNum �������������
//					if (searchNum == 0) {
//						if (rear > front) {
//							searchNum = rear - front - 1;
//						}
//						else {
//							searchNum = rear + MAXSIZE - front - 1;
//						}
//					}
//					else {
//						searchNum--;
//					}
//
//				
//
//					break;
//				}
//				else {
//					front = (front + 1) % MAXSIZE;
//					popcnt++;
//
//					//�̶����׻�˻�������� searchNum==0����
//					if (searchNum == 0) {
//						printf("%d\n", popcnt);
//						flag = 1;
//						break;
//					}
//
//					//searchNum �������������
//					if (searchNum == 0) {
//						if (rear > front) {
//							searchNum = rear - front - 1;
//						}
//						else {
//							searchNum = rear + MAXSIZE - front - 1;
//						}
//					}
//					else {
//						searchNum--;
//					}
//				}
//			}
//			if (flag == 1)
//				break;
//
//		}
//
//
//	}
//
//	return 0;
//}



#include <stdio.h>

#define MAXSIZE 102

long queue[MAXSIZE];
void initQueue();
void enqueue(int num);
long dequeue();
int isEmpty();
int front = 0, rear = 0;

int main() {
	int testcase;
	scanf("%d", &testcase);

	
	for (int i = 0; i < testcase; i++) {
		int popcnt = 0;
		initQueue();
		int totalCount, indexNum;
		scanf("%d %d", &totalCount, &indexNum);
		//���࿡ indexNum ==0 �̶�� 0��° ���Ҹ� �����ϰڴٴ°��� �ǹ��մϴ�.

		//totalCount�� ���࿡ 4��� 4���� ���Ҹ� ť�� �ְڴٴ°��� �ǹ��մϴ�.
		for (int j = 0; j < totalCount; j++) {
			int inputNum;
			scanf("%d", &inputNum);
			enqueue(inputNum);
		}

		while (1) {
			if (isEmpty()) {
				//ť������ٸ� ����
				//������ ������Ư���� ���⼭ ����Ǹ� �ȵɵ�. �ٸ� �ݺ�Ż�ⱸ���� �ʿ��ҵ�
				break;
			}
			else {
				int flag = 0;
				long temp = dequeue();
				int sizeQ=0;
				//�ݺ�ī��Ʈ���
				if (rear > front) { //TO DO ������쿡���ؼ� �����غ����ҵ�, ���ٸ� sizeQ=0;
					sizeQ = rear - front; //-1������
				}
				else if (rear == front) {
					//�������� ��µ̳���
					sizeQ = 0;
				}
				else
				{
					sizeQ = rear + MAXSIZE - front;//-1������
				}
				//�ݺ����� ���鼭 �̰ͺ��� �ڿ� �ִ� ���ڰ� �� ū ���� �ִ��� Ȯ����.


				for (int k = 0; k < sizeQ; k++) {
					//�ڿ� ������ ū ���ڰ� �ִ����� Ȯ���ϸ�˴ϴ�
					if (temp < queue[(front + k)%MAXSIZE]) {
						flag = 1;
						break;
					}
				}

				if (flag == 1) {
					enqueue(temp);
					if (indexNum == 0) {
						indexNum = sizeQ;
					}
					else {
						indexNum--;
					}
				}
				else {
					
					popcnt++;
					if (indexNum == 0) {
						printf("%d\n", popcnt);
						break;
					}
					
					indexNum--;

				}
				// flag = 1 �γ��´ٸ� ������ ū ���ڰ� �ִ°��̹Ƿ� ���� �ڷ� �ٽ� enqueue �մϴ�.
				//flag =0 �̶�� ������ �ڿ� ū ���ڰ� ���°��̹Ƿ� dequeue ���ѹ����� popcnt�� 1����
				//���� indexNum ==0 �̸鼭 flag =0�̶�� �׼��ڸ� ã���־����Ƿ� popcnt ����� break;  

				//pop���ϸ鼭 ���࿡ indexNum==0�̶�� ã�� ���ڰ� �°� �ű⼭ �극��ũ���,popī��Ʈ���
				//���������� popcnt�� ����ϴ°��Դϴ�.
			}
		}
	}

	return 0;
}


void initQueue() {
	for (int i = 0; i < MAXSIZE; i++) {
		queue[i] = 0;
	}
	front = 0;
	rear = 0;
}
void enqueue(int num) {
	if (rear + 1%MAXSIZE == front) {
		//printf("ť�� �����µ���");
		return;
	}
	queue[rear] = num;
	rear = (rear + 1) % MAXSIZE;
}
long dequeue() {
	if (isEmpty()) {
		//printf("ť��...����µ���");
	}
	int temp = queue[front];
	front = (front + 1) % MAXSIZE;
	return temp;
}
int isEmpty() {
	if (front == rear) {
		return 1;
	}
	else {
		return 0;
	}
}