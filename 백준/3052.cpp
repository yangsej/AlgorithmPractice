#include <stdio.h>

int main()
{
    int i, input, p, c = 0;
    bool a[42] = {false};

    for (i = 0; i < 10; i++)
    {
        scanf("%d", &input);
        p = input % 42;
        if (!a[p])
        {
            a[p] = true;
            c++;
        }
    }

    printf("%i\n", c);

    return 0;
}