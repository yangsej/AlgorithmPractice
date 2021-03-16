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
	int *a;
	int i;
	int K;
	int jump;
	int dist_sum;
	int distance;

	scanf("%d", &T);
	if (T < 1 || T > 5){
		return 1;
	}

	for (test_case = 1; test_case <= T; test_case++) {
		dist_sum = 0;
		distance = 0;
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
		scanf("%d", &N);
		if (N < 1 || N > 1000000){
			return 2;
		}

		a = (int*)malloc(sizeof(int)*N);
		if (a == NULL){
			return 3;
		}

		for (i = 0; i < N; i++){
			scanf("%d", &a[i]);
			if (a[i] < 1 || a[i] > pow(10, 9)){
				return 4;
			}
		}

		scanf("%d", &K);
		if (K < 1 || K > pow(10, 9)){
			return 5;
		}

		jump = 1;
		for (i = 0; i < N; i++){
			if (i>0){
				distance = a[i] - a[i - 1];
			}
			else{
				distance = a[0];
			}
			if (distance > K){
				jump = -1;
				break;
			}
			else{
				dist_sum += distance;
			}
			if (dist_sum > K){
				dist_sum = distance;
				jump++;
			}
		}

		// �� �κп��� ������ ����Ͻʽÿ�.
		printf("Case #%d\n", test_case);
		printf("%i\n", jump);
		free(a);
	}
	return 0;	// �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}