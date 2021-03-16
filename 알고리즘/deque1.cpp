#include <iostream>
#include <deque>
using namespace std;
int main()
{
    deque<double> dq;
    dq.push_front(1.1);
    dq.push_front(2.2);
    dq.push_front(3.3);
    // 3.3 2.2 1.1
    for (auto i = 0; i < dq.size(); i++)
        cout << dq[i] << endl;
    // 2.2
    dq.pop_front();
    cout << dq[1] << endl;
    return 0;
}