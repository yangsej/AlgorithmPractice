#include <stdio.h>

int main()
{
    int a[5] = {0}, i, j, max = 0, in;

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 4; j++)
        {
            scanf("%d", &in);
            a[i] += in;
        }

        if (a[i] > a[max])
            max = i;
    }

    printf("%i %i\n", max+1, a[max]);

    return 0;
}