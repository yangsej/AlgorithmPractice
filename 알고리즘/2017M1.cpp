#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int A[] = {3, 1, 4, 1, 5, 9, 2};
    vector<int> V;
    for(auto i: A) V.push_back(i);
    sort(V.begin(), V.end());
    for(auto i: V) cout << i << " ";
    cout << endl;
    return 0;
}