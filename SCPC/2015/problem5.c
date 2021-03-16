#include <stdio.h>
#include <stdlib.h>

int main(void) {
	/* �Ʒ� freopen �Լ��� input.txt�� read only �������� ����, ǥ���Է�(Ű����) ��� input.txt �� ���� �о���ڴٴ� �ǹ��� �ڵ��Դϴ�.
	���� ���� PC ���� �׽�Ʈ �� ����, �Է°��� input.txt�� ������ �� freopen �Լ��� ����ϸ�
	�� �Ʒ����� scanf �Լ��� ����Ͽ� ǥ���Է� ��� input.txt ���Ϸ� ���� �Է°��� �о� �� �� �ֽ��ϴ�.
	����, ���� PC���� freopen �Լ��� ������� �ʰ� ǥ���Է��� ����Ͽ� �׽�Ʈ�ϼŵ� �����մϴ�.
	��, Codeground �ý��ۿ��� "�����ϱ�" �� ������ �ݵ�� freopen �Լ��� ����ų� �ּ�(//) ó�� �ϼž߸� �մϴ�. */
	// freopen("input.txt", "r", stdin);

	/* setbuf �Լ��� ������� ������, ������ ���α׷��� ���� '�ð� �ʰ�'�� ���� ���� �Ǿ��� ��,
	printf�� ����� ������ ä������ �ʰ� '0��'�� �� ���� �ֽ��ϴ�.
	�ð� �ʰ� ������ ����� ��� ������ �ް��� �ϽŴٸ� "setbuf(stdout, NULL);" �� ����Ͻñ� �ٶ��ϴ�. */
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
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
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
					a[j][N] = i;// i�࿡�� ���� 0�� �ƴ� ���� ���� j���� ã�� N���� �ӽ� ����
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

		// �� �κп��� ������ ����Ͻʽÿ�.
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
	return 0;	// �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}
