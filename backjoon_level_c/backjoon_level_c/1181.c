//#include <stdio.h>
//#include <string.h>
//
//char arr[20000][51];
//int main() {
//	int num;
//
//	scanf("%d", &num);
//
//	//입력받자
//	for (int i = 0; i < num; i++) {
//		scanf("%s", arr[i]);
//	}
//	int len1;
//	int len2;
//	for (int i = 0; i < num - 1; i++) {
//		for (int j = 0; j < num -i -1; j++) {
//			
//			len1 = strlen(arr[j]);
//			len2 = strlen(arr[j + 1]);
//
//			if (len1 > len2) {
//				char temp[51];
//				strcpy(temp, arr[j]);
//				strcpy(arr[j], arr[j+1]);
//				strcpy(arr[j+1], temp);
//
//			}
//			else if ((len1 == len2) && strcmp(arr[j],arr[j+1])>0) {
//				char temp[51];
//				strcpy(temp, arr[j]);
//				strcpy(arr[j], arr[j + 1]);
//				strcpy(arr[j + 1], temp);
//			}
//		}
//	}
//
//	for (int i = 0; i < num; i++) {
//		if (strcmp(arr[i], arr[i + 1]) == 0) {
//			continue;
//		}
//		printf("%s\n", arr[i]);
//	}
//
//	return 0;
//}




//위에는 버블정렬로 정렬해보려고했는데 시간초과때문에 실패함 
//qsort를 사용하자.


#include <stdio.h>
#include <stdlib.h>

char arr[20000][51];

int comparelen(const void *a, const void *b) {

	int len1 = strlen((char *)a);
	int len2 = strlen((char *)b);
	
	if (len1 > len2)
		return 1;
	if (len2 > len1)
		return -1;

	return 0;
}

int comparestr(const void *a, const void *b) {


	int val = strcmp((char*)a, (char*)b);
	if (val > 0) {
		return 1;
	}
	else if (val < 0) {
		return -1;
	}


	return 0;
}

int main() {

	int input;
	scanf("%d", &input);

	for (int i = 0; i < input; i++) {
		scanf("%s", arr[i]);
	}
	qsort(arr, input, sizeof(arr[0]), comparelen);
	qsort(arr, input, sizeof(arr[0]), comparestr);
	
	for (int i = 0; i < input; i++) {
		if (strcmp(arr[i], arr[i + 1]) == 0) {
			continue;
		}
		printf("%s\n", arr[i]);
	}
	return 0;
}