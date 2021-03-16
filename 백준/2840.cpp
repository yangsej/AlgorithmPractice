#include <stdio.h>

int main()
{
    int i, N, K, r, s = 0;
    char C[26] = "?????????????????????????", in;

    scanf("%d%d", &N, &K);
    for (i = 0; i < K; i++)
    {
        scanf("%d", &r);
        s = (N + s - r) % N;
        scanf("%*c%c%*c", &in);
        if(C[s] == '?') C[s] = in;
        else if(C[s] != in) {
            printf("!\n");
            return 0;
        }
    }

    for (i = 0; i < N; i++)
    {
        printf("%c", C[(i + s) % N]);
    }
    printf("\n");

    return 0;
}