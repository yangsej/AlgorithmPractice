#include <stdio.h>
#include <stdlib.h>

int main(void) {
	/* 아래 freopen 함수는 input.txt를 read only 형식으로 열고, 표준입력(키보드) 대신 input.txt 로 부터 읽어오겠다는 의미의 코드입니다.
	만약 본인 PC 에서 테스트 할 때는, 입력값을 input.txt에 저장한 후 freopen 함수를 사용하면
	그 아래에서 scanf 함수를 사용하여 표준입력 대신 input.txt 파일로 부터 입력값을 읽어 올 수 있습니다.
	또한, 본인 PC에서 freopen 함수를 사용하지 않고 표준입력을 사용하여 테스트하셔도 무방합니다.
	단, Codeground 시스템에서 "제출하기" 할 때에는 반드시 freopen 함수를 지우거나 주석(//) 처리 하셔야만 합니다. */
	// freopen("input.txt", "r", stdin);

	/* setbuf 함수를 사용하지 않으면, 본인의 프로그램이 제한 '시간 초과'로 강제 종료 되었을 때,
	printf로 출력한 내용이 채점되지 않고 '0점'이 될 수도 있습니다.
	시간 초과 전까지 실행된 결과 점수를 받고자 하신다면 "setbuf(stdout, NULL);" 를 사용하시기 바랍니다. */
	setbuf(stdout, NULL);

	int T;
	int test_case;
	int N;
	int M;
	int i;
	int j;
	int no_money;
	int **a;
	int *b;
	int temp[3];

	scanf("%d", &T);
	if (T < 1 || T > 20){
		return 1;
	}

	for (test_case = 1; test_case <= T; test_case++) {
		// 이 부분에서 알고리즘 프로그램을 작성하십시오. 기본 제공된 코드를 수정 또는 삭제하고 본인이 코드를 사용하셔도 됩니다.
		no_money = 0;
		scanf("%d%d", &N,&M);
		if (N < 1 || N > 1000 || M < 1 || M > 5000){
			return 2;
		}

		a = (int**)malloc(sizeof(int*)*N);
		b = (int*)malloc(sizeof(int)*N);
		for (i = 0; i < N; i++){
			a[i] = (int*)malloc(sizeof(int)*(N+1));
		}
		if (a == NULL || b == NULL){
			return 3;
		}

		for (i = 0; i < N; i++){
			b[i] = -1;
			for (j = 0; j < N+1; j++){
				a[i][j] = 0;
			}
		}

		for (i = 0; i < M; i++){
			scanf("%d%d%d", &temp[0], &temp[1], &temp[2]);
			if (temp[0] < 1 || temp[0] > 1000 || temp[1] < 1 || temp[1] > 5000 || temp[2]<1 || temp[2]>10000){
				return 4;
			}
			a[temp[0] - 1][temp[1] - 1] = temp[2];
			a[temp[1] - 1][temp[0] - 1] = temp[2];
		}
		

		for (j = 1; j < N; j++){
			for (i = 0; i < j; i++){
				if (a[i][j] != 0 && (a[j][N]==-1 || a[j][N]>a[i][j])){
					a[j][N] = i;// i행에서 값이 0이 아닌 가장 작은 j열을 찾아 N열에 임시 저장
				}
			}

			for (i = 0; i < N; i++){
				if (a[j][i]!=0){
					a[j][i] += a[a[j][N]][j];
				}
			}
			b[a[j][N]]++;
		}

		for (i = 0; i < N; i++){
			if (a[i][N] == -1){
				for (j = i+1; j < N; j++){
					if (a[j][i] != 0 && a[i][N] == -1){
						a[i][N] = j;
					}
					else if (a[j][i] != 0 && a[i][N]>a[j][i]){
						a[i][N] = j;
					}
				}
			}

			for (j = 0; j < N; j++){
				if (a[i][j] != 0){
					a[i][j] += a[i][a[i][N]];
				}
			}
			b[a[i][N]]--;
		}

		for (j = 0; j < N; j++){
			if (b[j] <= 1){
				no_money++;
			}
		}

		// 이 부분에서 정답을 출력하십시오.
		printf("Case #%d\n", test_case);
		printf("%i", no_money);
		for (i = 0; i < N; i++){
			if (b[i]<=1){
				printf(" %i", i+1);
			}
		}
		printf("\n");
		free(a);
	}
	return 0;	// 정상종료 시 반드시 0을 리턴해야 합니다.
}
