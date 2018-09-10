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
//		//searchNum ==2 라면 2번째 원소가 몇번째에 출력되는지 
//		//popcnt는 몇번째 출력됬는지 알려줄것입니다.
//
//		int front = 0, rear = 0;
//		for (int j = 0; j < num; j++) {
//			scanf("%d", &printer[j]);
//
//			queue[rear++] = printer[j];
//		}
//
//
//		while (front<rear) { // 큐안에값이들어가있다면
//			int flag = 0;
//			int popcnt = 0;
//			int pop = queue[front];
//			front++;
//			for (int k = front; k < rear; k++) {
//				if (queue[k] > pop) {
//					//뒤에 나보다 큰 우선순위를 가진애가있음
//					queue[rear] = pop;
//					rear++;
//					flag = 1; // 출력이 아님. 뒤에넘어갔다는것
//					if (searchNum == 0) {
//						//searchNum이 뒤로갔다는소리니까
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
//					//다시 맨뒤에 넣는과정 
//					
//				}
//				else {
//					if (searchNum == 0) {
//						//searchNum이 뒤로갔다는소리니까
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
//				//제일 큰값이 앞에있었고 정상출력
//				printf("popcnt 증가했습니다\n");
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
//int queue[MAXSIZE]; //% 연산자필요
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
//		//테스트 케이스 갯수의 해당하는 반복문
//		scanf("%d ", &num );
//		scanf("%d ", &searchNum );
//		//searchNum ==2 라면 2번째 원소가 몇번째에 출력되는지 
//		//popcnt는 몇번째 출력됬는지 알려줄것입니다.
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
//			int popcnt = 0; //출력값
//			int temp = queue[front];
//			int flag = 0;
//			int cnt = rear; 
//			for (int k = front; k < cnt; k = (k + 1) % MAXSIZE) {
//				if (queue[k] < queue[k+1]) {
//					//더큰 우선순위의 프린트가있으므로 맨뒤로넣자
//					queue[rear] = temp;
//					rear = (rear + 1) % MAXSIZE;
//					front = (front + 1) % MAXSIZE;
//
//					//searchNum 포지션잡아주자
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
//					//이때는항상검사해줘야함 searchNum==0인지
//					if (searchNum == 0) {
//						printf("%d\n", popcnt);
//						flag = 1;
//						break;
//					}
//
//					//searchNum 포지션잡아주자
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
		//만약에 indexNum ==0 이라면 0번째 원소를 추적하겠다는것을 의미합니다.

		//totalCount가 만약에 4라면 4개의 원소를 큐에 넣겠다는것을 의미합니다.
		for (int j = 0; j < totalCount; j++) {
			int inputNum;
			scanf("%d", &inputNum);
			enqueue(inputNum);
		}

		while (1) {
			if (isEmpty()) {
				//큐가비었다면 종료
				//하지만 문제의특성상 여기서 종료되면 안될듯. 다른 반복탈출구간이 필요할듯
				break;
			}
			else {
				int flag = 0;
				long temp = dequeue();
				int sizeQ=0;
				//반복카운트계산
				if (rear > front) { //TO DO 같을경우에대해서 생각해봐야할듯, 같다면 sizeQ=0;
					sizeQ = rear - front; //-1지우자
				}
				else if (rear == front) {
					//마지막에 출력됫네유
					sizeQ = 0;
				}
				else
				{
					sizeQ = rear + MAXSIZE - front;//-1지우자
				}
				//반복문을 돌면서 이것보다 뒤에 있는 숫자가 더 큰 값이 있는지 확인함.


				for (int k = 0; k < sizeQ; k++) {
					//뒤에 나보다 큰 숫자가 있는지만 확인하면됩니다
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
				// flag = 1 로나온다면 나보다 큰 숫자가 있는것이므로 제일 뒤로 다시 enqueue 합니다.
				//flag =0 이라면 나보다 뒤에 큰 숫자가 없는것이므로 dequeue 시켜버리고 popcnt를 1증가
				//만약 indexNum ==0 이면서 flag =0이라면 그숫자를 찾고있었으므로 popcnt 출력후 break;  

				//pop을하면서 만약에 indexNum==0이라면 찾는 숫자가 맞고 거기서 브레이크찍고,pop카운트출력
				//최종적으로 popcnt를 출력하는것입니다.
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
		//printf("큐가 꽉찻는데유");
		return;
	}
	queue[rear] = num;
	rear = (rear + 1) % MAXSIZE;
}
long dequeue() {
	if (isEmpty()) {
		//printf("큐가...비엇는데유");
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