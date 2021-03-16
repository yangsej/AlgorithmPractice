#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Book
{
public:
    int no;
    int score;

    bool operator<(Book b) const{
        return this->score < b.score;
    }
};

int B = 0, L = 0, D = 0, N[100000] = {0}, T[100000] = {0}, M[100000] = {0};
Book S[100000];
vector<Book> lib_books[100000];

int scaned_books[100000] = {0};

int main(int argc, char *argv[])
{
    // 입력
    ifstream in(argv[1]);
    if (in.is_open())
    {
        in >> B >> L >> D;

        for (int i = 0; i < B; i++)
        {
            S->no = i;
            in >> S->score;
        }

        for (int i = 0; i < L; i++)
        {
            in >> N[i] >> T[i] >> M[i];
            for (int j = 0; j < N[i]; j++)
            {
                int index = 0;
                in >> index;
                lib_books[i][j] = S[index];
            }
            sort(lib_books[i].begin(), lib_books[i].end(), );
        }
        in.close();
    }

    // 풀이

    // 출력
    string s = argv[1];
    s.append(".out");
    ofstream out(s);
    if (out.is_open())
    {
        out << B << L << D;

        for (int i = 0; i < B; i++)
        {
            out << S[i];
        }

        for (int i = 0; i < L; i++)
        {
            out << N[i] << T[i] << M[i];
            for (int j = 0; j < N[i]; j++)
            {
                out << books[i][j];
            }
        }
        out.close();
    }
    return 0;
}