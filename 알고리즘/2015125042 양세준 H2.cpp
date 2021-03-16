#include <cstdio>

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    int *A = new int[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &A[i]);
    }

    int *sumA = new int[n];
    sumA[0] = A[0];
    if (sumA[0] < 0)
        sumA[0] = 0;
    for (int i = 1; i < n; i++)
    {
        sumA[i] = sumA[i - 1] + A[i];
        if (sumA[i] < 0)
            sumA[i] = 0;
    }

    int *sumkA = new int[n]{0};
    for (int i = 0; i < k; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            sumkA[i] += A[j];
        }
    }
    for (int i = k; i < n; i++)
    {
        sumkA[i] = sumkA[i - 1] + A[i] - A[i - k];
    }

    
    int result = sumkA[k-1];
    for (int i = k; i < n; i++)
    {
        A[i] = sumA[i - k] + sumkA[i];
        if (result < A[i])
            result = A[i];
    }

    printf("%i\n", result);

    delete A, sumA, sumkA;
    return 0;
}