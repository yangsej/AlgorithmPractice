#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int m, n;
long long max_num = 0;
vector<int> slice(100001);
vector<int> num(100001);
vector<int> result;
vector<int> arr;

int combination(int n, int k, int temp)
{
    //vector<int> num;
    long long sum;
    long long ans = 0;
    for (int i = 0; i < n; i++)
    {
        //num.push_back(i+1);
        num[i] = slice[i];
    }
    vector<int> ind;
    for (int i = 0; i < k; i++)
    {
        ind.push_back(1);
    }
    for (int i = 0; i < n - k; i++)
    {
        ind.push_back(0);
    }
    sort(ind.begin(), ind.end());
    //순열
    do
    {
        sum = 0;
        for (int i = 0; i < ind.size(); i++)
        {
            if (ind[i] == 1)
            {
                // cout << num[i] << " ";
                sum = sum + num[i];
                result.push_back(i);
            }
        }
        // cout << endl;
        if (sum != temp)
            result.clear();
        else
        {
            for (int i = 0; i < result.size(); i++)
            {
                arr.push_back(result[i]);
            }
        }
        if (sum <= m)
        {
            ans = max(ans, sum);
            // if(max_num<sum)
            // {
            //     max_num=sum;
            //     result.push_back(9999);
            //     continue;
            // }
            // else
            // {
            //     result.clear();
            // }
        }
    } while (next_permutation(ind.begin(), ind.end()));
    return ans;
}

int main(int argc, char *argv[])
{
    ios_base::sync_with_stdio(false);

    cin.tie(NULL);

    ifstream in(argv[1]);
    if (in.is_open())
    {
        in >> m >> n;

        for (int i = 0; i < n; i++)
        {
            in >> slice[i];
        }
        in.close();
    }
    else
    {
        cout << "파일을 찾을 수 없습니다!" << endl;
    }

    long long tmp;
    long long ans = 0;
    int size;

    int mintype = 1, minsum = 0, maxtype = n, maxsum = 0;
    for (;; maxtype++)
    {
        maxsum += slice[maxtype - 1];
        if (maxsum > m)
            break;
    }
    for (int i = n - 1; i > 0; i--)
    {
        minsum += slice[i];
        if (minsum > m)
        {
            mintype = n - i;
            break;
        }
    }
    cout << mintype << " " << minsum << " " << maxtype << " " << maxsum << endl;
    for (int i = mintype; i <= maxtype; i++)
    {
        cout << i << endl;
        tmp = combination(n, i, -1);
        //cout<<tmp<<endl;
        if (ans < tmp)
        {
            ans = tmp;
            size = i;
        }
    }

    //cout<<ans<<endl;
    string s = argv[1];
    s.append(".out");
    ofstream out(s);
    if (out.is_open())
    {
        out << size << endl;
        combination(n, size, ans);
        for (int i = 0; i < arr.size(); i++)
        {
            out << arr[i] << " ";
        }
        out << endl;
        out.close();
    }
    else
    {
        cout << "파일을 찾을 수 없습니다!" << endl;
    }

    return 0;
}