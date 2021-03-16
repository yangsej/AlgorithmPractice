#include <stdio.h>

int main(int argc, char **argv)
{
    // input
    // ● an integer M ( 1 ≤ M ≤ 10 ^ 9 ) – the maximum number of pizza slices to order
    // ● an integer N ( 1 ≤ N ≤ 10 ^ 5 ) – the number of different types of pizza
    int i = 0, j = 0, M = 0, N = 0, K = 0;
    int types[10000] = {0}, result[10000] = {0};

    FILE *pFile = NULL;
    pFile = fopen(argv[1], "r");
    if (pFile == NULL)
    {
        printf("Failed to open file %s\n", argv[1]);
        return -1;
    }

    fscanf(pFile, "%d%d", &M, &N);
    printf("%i %i\n", M, N);

    for (i = 0; i < N; i++)
    {
        fscanf(pFile, "%d", &types[i]);
        printf("%i ", types[i]);
    }
    printf("\n");

    // solution

    // 가장 큰 것을 먼저 골라 1개, 2개, ... x개를 고르는 경우를 계속 진행한다.
    int ans = types[N - 1];

    int combination[10000] = {0};
    combination[0] = N-1;
    int index = 1;
    bool done = false;
    // for (K = 2; K <= N; K++)
    // {
    // }

    for (j = N - 1; j > 1; j--)
    {
        int high = 0;
        for(int k = 0; k < index; k++){
            high += types[combination[k]];
        }
        for (i = N - 2; i > 0; i--)
        {
            int low = types[i];
            int temp = high + low;
            printf("%i + %i = %i\n", high, low, temp);

            if (temp == M) // 적절
            {
                ans = temp;
                combination[index++] = i;
                combination[index++] = j;
                done = true;
                break;
            }
            else if (temp < M) // 적음
            {
                if (temp > ans) // 신기록
                {
                    ans = temp;
                    index -= 2;
                    combination[index++] = i;
                    combination[index++] = j;
                } else{
                    done = true;
                }
                break;
            }
        }
        if (done)
            break;
    }

    // output
    printf("%i\n", ans);

    printf("%i\n", K);
    // for (i = 0; i < K; i++)
    // {
    //     printf("%i ", result[i]);
    // }
    // printf("%i\n", K);

    return 0;
}