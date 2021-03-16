#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, k;
    scanf("%i %i", &n, &k);

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        scanf("%i", &v[i]);

    sort(v.begin(), v.end());

    int var = 0, count = 0, i;
    for (i = 0; i < n; i++)
    {
        if (v[i] != var)
        {
            var = v[i];
            count = 0;
        }
        count++;

        if (count >= k)
            break;
    }
    if (i == n)
        var = -1;
    printf("%i\n", var);

    return 0;
}