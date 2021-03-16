#include <iostream>
#include <vector>
int main()
{
    std::vector<int> A;
    std::vector<int>::iterator it;
    A.push_back(1);
    A.push_back(2);
    A.push_back(3);
    for (it = A.begin(); it != A.end(); it++)
        std::cout << *it << std::endl;
    for (int i = 0; i < A.size(); i++)
        std::cout << A[i] << std::endl;
    return 0;
}