#include <cstdio>

int main()
{
    int M, N, i, j, k, c[100][100] = {0}, b[5] = {0};
    char l[502];
    scanf("%d%d", &M, &N);

    b[0] = M * N;
    for (i = 0; i < M; i++)
    {
        scanf("%s", l);
        for (k = 0; k < 4; k++)
        {
            scanf("%s", l);
            for (j = 0; j < N; j++)
            {
                if (l[j * 5 + 1] == '*')
                {
                    b[k]--;
                    b[k + 1]++;
                }
            }
        }
    }
    scanf("%s", l);

    printf("%i %i %i %i %i\n", b[0], b[1], b[2], b[3], b[4]);

    return 0;
}