#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Activity
{
public:
    int index;
    pair<int, int> time;
    char person;

    Activity()
    {
        index = -1;
        time.first = 0;
        time.second = 0;
    }

    Activity(int index, int start, int end)
    {
        this->index = index;
        this->time.first = start;
        this->time.second = end;
    }
};

bool compareIndex(Activity &first, Activity &second)
{
    return first.index < second.index;
}

bool compareTime(Activity &first, Activity &second)
{
    return first.time < second.time;
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int x = 1; x <= T; x++)
    {
        int N, S, E;
        vector<Activity> Activities;

        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
        {
            scanf("%d%d", &S, &E);
            Activities.push_back(Activity(i, E, S));
        }
        sort(Activities.begin(), Activities.end(), compareTime);

        string y;
        Activity C, J;
        for (Activity &a : Activities)
        {
            if (C.time.first <= a.time.second)
            {
                a.person = 'C';
                C = a;
            }
            else if (J.time.first <= a.time.second)
            {
                a.person = 'J';
                J = a;
            }
            else
            {
                y = "IMPOSSIBLE";
                break;
            }
        }

        if (y != "IMPOSSIBLE")
        {
            sort(Activities.begin(), Activities.end(), compareIndex);
            for (Activity a : Activities)
            {
                y.push_back(a.person);
            }
        }

        printf("Case #%i: %s\n", x, y.c_str());
    }

    return 0;
}