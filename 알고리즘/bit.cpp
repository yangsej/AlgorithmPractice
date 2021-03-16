#include <iostream>
using namespace std;

class BIT
{

    int n, *tree, *A;
  public:
    BIT()
    {
        int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
        BIT(17, array);
    }
    BIT(int n, int* array)
    {
        this->n = n;
        this->tree = new int[n]{0};
        this->A = new int[n]{0};
        for (int i = 1; i < n; i++)
        {
            this->update(i, array[i]);
            // cout << A[i] << " " << tree[i] << endl;
        for (int j = 1; j < n; j++)
            cout << this->A[j] << " " << this->tree[j] << endl;
        }
        for (int j = 1; j < n; j++)
            cout << this->A[j] << " " << this->tree[j] << endl;
    }
    friend ostream &operator<<(ostream &os, const BIT &b)
    {
        for (int i = 1; i < b.n; i++)
            os << b.tree[i] << " ";
        return os;
    }
    int sum(int i)
    {
        int ans = 0;
        while (i > 0)
        {
            ans += tree[i];
            i -= (i & -i);
        }
        return ans;
    }

    void update(int i, int &num)
    {
        this->A[i] = num;
        int pre_tree = this->tree[i];
        while (i <= n)
        {
            // cout << i << ": " << this->A[i] << " " << this->tree[i] << endl;
            this->tree[i] += num - pre_tree;
            // cout << this->A[i] << " " << this->tree[i] << endl;
            i += (i & -i);
        }
    }
};

int main()
{
    BIT bitTree = BIT();
    // for(int i=1; i<17; i++)
    //     cout << "A : " <<bitTree.A[i] << endl;
    cout << bitTree << endl;
    // bitTree.update(1, 4);
    // cout << bitTree << endl;
    // bitTree.update(1, 2);
    // cout << bitTree << endl;
    return 0;
}