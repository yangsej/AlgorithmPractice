#include <cstdio>
#include <vector>
#include <algorithm>
#include <ctime>
using namespace std;

int main()
{
    int n, k;
    // scanf("%i %i", &n, &k);

    FILE *fp = fopen("C:/Python27/randomcount.txt", "r");
    fscanf(fp, "%i %i", &n, &k);
    vector<int> v(n);
    for (int i = 0; i < n; i++){
        fscanf(fp, "%i", &v[i]);
    }
    fclose(fp);

    // vector<int> v(n);
    // for (int i = 0; i < n; i++)
    //     scanf("%i", &v[i]);

    clock_t start = clock();
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
    printf("%0.5f\n", (float)(clock() - start) / CLOCKS_PER_SEC);
    return 0;
}