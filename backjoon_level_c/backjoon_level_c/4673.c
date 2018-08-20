/*#include <stdio.h>

int main() {

	int num = 1;

	int i,j, flag;

	int selfNum[10000] = {0,};

	while (1) {
		flag = 1;  // 중복제거를위해..

		if (num > 10000) {
			break;
		}

		//중복일때는 패스하려고, 이미들어가있으니까 안넣어도됨.
		for (i = 0; i < num; i++) {
			if (selfNum[i] == num + num / 10000 + num / 1000 + num / 100 + num / 10 + num % 10) {
				num++;
				flag = 0;
				break;
			}
		}
		if (flag == 1) {
			selfNum[num - 1] = num + num / 10000 + num / 1000 + num / 100 + num / 10 + num % 10;
			num++;
		}
		

		
	}




	for (i = 0; i < 10000; i++) {
		flag = 1;
		for (j = 0; j < 10000; j++) {
			if (i + 1 == selfNum[j]) {
				flag = 0;
				break;
			}
		}
		if (flag == 1)
			printf("%d\n", i + 1);

	}

	


	return 0;

}*/

/*
*180820 
*어려웟음..
*
*/

#include <stdio.h>

int main() {
	int selfNum[10000] = { 0, };

	int i,j;
	for (i = 1; i < 10001; i++) {
		
		//이코드 잘못됨
		//selfNum[i - 1] = i + (i / 10000) + (i / 1000) + (i / 100) + (i / 10) + (i % 10);
		int n = i;
		int sum = n;
		while (n) {
			sum = sum + n % 10;
			n = n / 10;
		}
		selfNum[i - 1] = sum;
	}
	int flag;
	for (i = 0; i < 10000; i++) {
		flag = 1;
		for (j = 0; j < 10000; j++) {
			if (selfNum[j] == i + 1) {
				flag = 0;
				break;
			}
		}
		// 1이라는 말은 selfNum 배열에 그 수가 없다는 뜻
		if (flag == 1) { 
			printf("%d\n", i + 1);
		}
	}
	return 0;
}