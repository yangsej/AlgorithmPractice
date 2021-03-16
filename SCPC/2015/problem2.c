#include <stdio.h>
#include <stdlib.h>
#include <math.h>


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
	int **a;
	int **b;
	int i;
	int j;
	int move[2];
	int temp;
	int current[2];
	int mirrors;

	scanf("%d", &T);
	if (T < 1 || T > 20){
		return 1;
	}

	for (test_case = 1; test_case <= T; test_case++) {
		move[0] = 0;
		move[1] = 1;
		current[0] = 0;
		current[1] = 0;
		mirrors = 0;
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
		scanf("%d", &N);
		if (N < 1 || N > 1000){
			return 2;
		}

		a = (int**)malloc(sizeof(int*)*N);
		b = (int**)malloc(sizeof(int*)*N);
		for (i = 0; i < N; i++){
			a[i] = (int*)malloc(sizeof(int)*N);
			b[i] = (int*)malloc(sizeof(int)*N);
		}
		if (a == NULL || b == NULL){
			return 3;
		}

		for (i = 0; i < N; i++){
			for (j = 0; j < N; j++){
				scanf("%1d", &a[i][j]);
				if (a[i][j] < 0 || a[i][j] > 2){
					return 4;
				}
			}
		}

		while ((current[0] >= 0 && current[0] < N) && (current[1] >= 0 && current[1] < N)){
			temp = move[0];
			if (a[current[0]][current[1]] == 1){

				move[0] = -move[1];
				move[1] = -temp;
				if (b[current[0]][current[1]] != 1){
					mirrors++;
					b[current[0]][current[1]] = 1;
				}
			}
			else if (a[current[0]][current[1]] == 2){
				move[0] = move[1];
				move[1] = temp;
				if (b[current[0]][current[1]] != 1){
					mirrors++;
					b[current[0]][current[1]] = 1;
				}
			}
			current[0] += move[0];
			current[1] += move[1];
		}

		// �� �κп��� ������ ����Ͻʽÿ�.
		printf("Case #%d\n", test_case);
		printf("%i\n", mirrors);
		free(a);
		free(b);
	}
	return 0;	// �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}