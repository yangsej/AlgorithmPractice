#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for (int x = 1; x <= T; x++)
    {
        string S="", y="";
        cin >> S;
        int i = 0;
        for(char c: S){
            int d = c - '0', j = 0, k = 0;
            j = y.find_last_not_of(")", i-1) + 1;
            if(j==-1) j=i;
            k = d-(i-j);
            if(k<0) {
                k=0;
                j = i-d;
            }

            y.insert(j, k, '(');
            y.insert(j+k, 1, c);
            y.insert(j+k+1, k, ')');

            i = i+k+k+1;
        }

        printf("Case #%i: %s\n", x, y.c_str());
    }

    return 0;
}