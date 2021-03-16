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
	int M;
	long *B;
	long temp;
	int i;
	int j;
	int check;
	int result;
	int zero_c;

	scanf("%d", &T);
	if (T<1 || T>30){
		return 1;
	}
	for (test_case = 1; test_case <= T; test_case++) {
		// �� �κп��� �˰��� ���α׷��� �ۼ��Ͻʽÿ�. �⺻ ������ �ڵ带 ���� �Ǵ� �����ϰ� ������ �ڵ带 ����ϼŵ� �˴ϴ�.
		scanf("%d", &M);
		if (M<2 || M>100000){
			return 2;
		}
		B = (long*)malloc(sizeof(long)*M);

		scanf("%li", &temp);
		B[0] = temp;
		zero_c = 0;
		for (i = 1; i < M; i++){
			scanf("%li", &B[i]);
			if (B[i] < temp){
				temp = B[i];
			}
			B[i - 1] = B[i] - B[i - 1];
			if (B[i-1] == 0){
				zero_c = 1;
			}
			if (zero_c == 1 && B[i-1] != 0){
				zero_c = 2;
				break;
			}
		}

		if (zero_c == 0){
			result = 0;
			if (temp>1){
				for (j = 1; j <= temp; j++){
					check = 0;
					for (i = 0; i < M - 1; i++){
						if (B[i] % j != 0){
							check = 1;
							break;
						}
					}
					if (check == 0){
						result++;
					}
				}
			}
			else if (temp == 1){
				result++;
			}
		}
		// �� �κп��� ������ ����Ͻʽÿ�.
		printf("Case #%d\n", test_case);
		if (zero_c == 0){
			printf("%i\n", result);
		}
		else if (zero_c == 2){
			printf("0\n");
		}
		else{
			printf("1\n");
		}
		free(B);
	}


	return 0;	// �������� �� �ݵ�� 0�� �����ؾ� �մϴ�.
}