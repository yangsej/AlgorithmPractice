#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


pair<int, int> minP;

bool compare(pair<int, int> &p1, pair<int, int> &p2)
{
    if(p1 == minP) return true;
    if(p2 == minP) return false;
    if(p1.first == p2.first == minP.first) return p1.second < p2.second;
    if(p1.first == minP.first || p2.first == minP.first) return p1.first > p2.first;
    if((p1.first - minP.first)*(p2.first - minP.first) < 0) return p1.first > p2.first;
    return (p1.second - minP.second) / (double)(p1.first - minP.first) < (p2.second - minP.second) / (double)(p2.first - minP.first);
}

long long cross(pair<int, int> &a, pair<int, int> &b, pair<int, int> &c){
    return b.first * c.second - b.first * a.second - a.first * c.second
        - c.first * b.second + c.first * a.second + a.first * b.second;
}

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    vector<pair<int, int>> A(n), B(m), hull;
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &A[i].first, &A[i].second);
    }
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &B[i].first, &B[i].second);
    }

    // 최저 찾기
    minP = B[0];
    for(pair<int, int> p : B){
        if(p.second < minP.second) minP = p;
        else if(p.second == minP.second && p.first > minP.first) minP = p;
    }
    
    // tan 기준 정렬
    sort(B.begin(), B.end(), compare);

    // 컨벡스 헐
    hull.push_back(B[0]);
    for(int i=0; i<m; i++){
        hull.push_back(B[(i+1)%m]);
        pair<int, int> a = hull[hull.size()-2], b = hull[hull.size()-1], c = B[(i+2)%m];
        if(cross(a, b, c) < 0){
            hull.pop_back();
            hull.push_back(c);
            i++;
        }
    }

    // 확인
    for(pair<int, int> p : A){
        char result = 'Y';
        for(int i=0; i<hull.size()-1; i++){
            pair<int, int> a = hull[i], b = hull[(i+1)%hull.size()];
            long long temp = cross(a, b, p);
            if(temp < 0){
                result = 'N';
                break;
            } else if(temp == 0){
                long long dot = (p.first-a.first) * (p.first-b.first) + (p.second-a.second) * (p.second-b.second);
                if(dot > 0) result = 'N';
                break;
            }
        }
        printf("%c", result);
    }
    printf("\n");
    
    return 0;
}
