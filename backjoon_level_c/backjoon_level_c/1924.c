#include <stdio.h>

int main() {
	int x, y;
	int date[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

	scanf("%d %d", &x, &y);

	int dayCheck=0; // %연산자 사용후 1일경우 MON, 2일경우 TUE, 0일경우 SUN 

	int i;
	for (i = 1; i < x; i++) {
		dayCheck = dayCheck + date[i-1];

	}
	dayCheck = dayCheck + y;
	dayCheck = dayCheck % 7;
	switch (dayCheck) {
	case 0:
		printf("SUN\n");
		break;
	case 1:
		printf("MON\n");
		break;
	case 2:
		printf("TUE\n");
		break;
	case 3:
		printf("WED\n");
		break;
	case 4:
		printf("THU\n");
		break;
	case 5:
		printf("FRI\n");
		break;
	case 6:
		printf("SAT\n");
		break;
	}

	return 0;
}