#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int B = 0, L = 0, D = 0, S[100000] = {0}, N[100000] = {0}, T[100000] = {0}, M[100000] = {0};
vector<int> books[100000];
int scaned_books[100000] = {0}, full_time[100000] = {0}, full_score[100000] = {0}, priority[100000] = {0};
vector<int> result;

int main(int argc, char *argv[])
{
    // 입력
    ifstream in(argv[1]);
    if (in.is_open())
    {
        in >> B >> L >> D;
        for (int i = 0; i < B; i++)
        {
            in >> S[i];
        }

        for (int i = 0; i < L; i++)
        {
            in >> N[i] >> T[i] >> M[i];
            for (int j = 0; j < N[i]; j++)
            {
                int temp = 0;
                in >> temp;
                books[i].push_back(temp);
            }
        }
        in.close();
    }

    // 풀이
    for (int i = 0; i < L; i++)
    {
        sort(books[i].begin(), books[i].end(),
             [](const int &x, const int &y) -> bool {
                 return S[x] > S[y];
             });

        full_time[i] = T[i] + N[i] / M[i];
        for (int j = 0; j < N[i]; j++)
        {
            full_score[i] += S[books[i][j]];
        }

        priority[i] = full_score[i] / full_time[i];
    }

    int lib_count = 0;
    while (D > 0 && lib_count < L)
    {
        int index = 0;
        for (int i = 1; i < L; i++)
        {
            if (priority[i] > priority[index])
            {
                index = i;
            }
        }

        if (D < full_time[index])
        {
            if(D <= T[index]) break;
            int book_scan = M[index] * (D - T[index]);
            if(book_scan < N[index]) N[index] = book_scan;
        }

        priority[index] = -1;
        D -= T[index];

        lib_count++;
        result.push_back(index);
    }

    // 출력
    string s = argv[1];
    s.append(".out");
    ofstream out(s);
    if (out.is_open())
    {
        out << lib_count << endl;

        for (int i = 0; i < lib_count; i++)
        {
            out << result[i] << " " << N[result[i]] << endl;
            for (int j = 0; j < N[result[i]]; j++)
            {
                out << books[i][j] << " ";
            }
            out << endl;
        }
        out.close();
    }
    return 0;
}