#include <stdio.h>
#include <math.h>


int num[8001]; //���ǹ����� -4000~4000
int sorted[500000];

int main() {
	int input; //1~500,000 ����

	scanf("%d", &input);
	int n;
	int sum = 0;
	for (int i = 0; i < input; i++) {
		scanf("%d", &n);
		sum = sum + n;
		num[n + 4000]++;
	}

	int k = 0;
	int i = 0;
	int max = -1;
	int maxk = -1;
	int flag = 0;
	while (1) {
		if (i == input) {
			break;
		}

		if (num[k] == max && flag ==0) {
			maxk = k;
			flag = 1;
		}
		else if (num[k]>max && flag ==0) {
			max = num[k];
			maxk = k;
		}
		while (num[k]--) {
			sorted[i] = num[k];
			i++;
		}

		k++;
	}
	printf("%f\n", ceil((float)sum / input - 0.5)); // ������
	printf("%d\n", sorted[(input - 1) / 2]); // �߾Ӱ�
	printf("%d\n", sorted[k]); //�ֺ� 
	printf("%d\n", sorted[input - 1] - sorted[0]);//���� ��� 

	return 0;


	//cell �� �ø��Լ�
	//floor  �����Լ�





}