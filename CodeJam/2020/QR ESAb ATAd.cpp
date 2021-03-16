#include <iostream>
#include <string>
using namespace std;

int T, B;
int first, last, numQuery, eq, neq;
bool rev, comp;
string A;

char query(int P)
{
    int p = P;
    if (rev)
        p = B - P - 1;

    // indicating which position in the array you wish to look at.
    printf("%i\n", p);
    fflush(stdout);

    // the value it currently has stored at bit position P
    char bit;
    scanf("%c", &bit);

    if (comp)
        bit = bit == '0' ? '1' : '0';

    A[P] = bit;
    numQuery++;
    return bit;
}

void findParity()
{
    while (eq < 0 || neq < 0)
    {
        if (first == B / 2)
            break;

        char a = query(first), b = query(B - first - 1);
        if (a == b && eq < 0)
            eq = first;
        else if (a != b && neq < 0)
            neq = first;
        first++;
    }
    last = first;
}

void checkEffect()
{
    char a0, a1, b0, b1;
    a0 = A[eq];
    b0 = A[neq];

    a1 = query(eq);
    b1 = query(neq);
    if (a0 == a1)
    {
        if (b0 == b1)
            return;
        else
            rev = !rev;
    }
    else
    {
        if (b0 == b1)
        {
            comp = !comp;
            rev = !rev;
        }
        else
            comp = !comp;
    }
}

int main()
{
    scanf("%d%d", &T, &B);

    for (int x = 1; x <= T; x++)
    {
        first = 0, last = 0, numQuery = 0, eq = -1, neq = -1;
        rev = false, comp = false;
        string a;

        findParity();
        while (numQuery < 150)
        {
            if (numQuery % 10 == 1)
            {
                checkEffect();
            }
            else
            {
                query(first++);
            }
        }

        cout << a << endl;
        cout.flush();

        // whether your answer was correct
        char response;
        scanf("%c", &response);
        if (response == 'N')
            return 1;
    }
    return 0;
}
