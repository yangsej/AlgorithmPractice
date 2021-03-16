#include <stdio.h>

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
	int a;
	int b;
	int c;
	int N;
	int K;
	int i;
	int result[7];
	int turn;

	scanf("%d", &T);
	if (T<1 || T>40){
		return 1;
	}
	for (test_case = 1; test_case <= T; test_case++) {
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
		scanf("%i%i%i", &a, &b, &c);
		if (b<1 || b>a || a > 10000 || c<1 || c>7){
			return 2;
		}
		for (i = 0; i < 7; i++){
			result[i] = 0;
		}
		turn = 1;
		for (i=0; i < c; i++){
			scanf("%i%i", &N, &K);
			if (N<2 || N>1000000 || K<1 || K>1000){
				return 3;
			}
			if ((N - 1) % (K*(a + b) + 1)>0 && (N - 1) % (K*(a + b) + 1) < K*a){
				result[i] = turn;
			}
			else{
				result[i] = -turn;
			}
			turn = -turn;
		}



		// �� �κп��� ������ ����Ͻʽÿ�.
		printf("Case #%d\n", test_case);
		for (i = 0; i < c; i++){
			if (result[i] == 1){
				printf("a");
			}
			else{
				printf("b");
			}
		}
		puts("");
	}
	return 0;	// �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}