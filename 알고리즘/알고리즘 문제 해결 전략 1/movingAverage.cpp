#include <vector>
#include <stdio.h>

using namespace std;

vector<double> movingAverage(const vector<double> &A, int M)
{
    int N = A.size();
    vector<double> answer;

    double partialSum = 0;
    for (int i = 0; i < M-1; i++)
    {
        partialSum += A[i];
        answer.push_back(0);
    }

    for (int i = M; i < N; i++)
    {
        partialSum -= A[i - M];
        partialSum += A[i];
        answer.push_back(partialSum / M);
    }
    return answer;
}

int main()
{
    vector<double> a = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    vector<double> mv = movingAverage(a, 4);
    for(double d : mv) printf("%lf\n", d);
    return 0;
}