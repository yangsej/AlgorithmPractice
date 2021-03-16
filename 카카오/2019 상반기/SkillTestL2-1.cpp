#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

struct filename
{
    string head, tail;
    int number;
};

bool compare(string a, string b)
{
    char *numbers = "0123456789";
    string at = a.c_str(), bt = b.c_str();

    filename aname, bname;

    transform(at.begin(), at.end(), at.begin(), [](unsigned char c) { return tolower(c); });
    transform(bt.begin(), bt.end(), bt.begin(), [](unsigned char c) { return tolower(c); });

    int first = at.find_first_of(numbers), last = at.find_first_not_of(numbers, first);
    aname.head = at.substr(0, first);
    if (last > -1)
    {
        aname.number = stoi(at.substr(first, last - first));
        aname.tail = at.substr(last);
    }
    else
    {
        aname.number = stoi(at.substr(first));
    }

    first = bt.find_first_of(numbers), last = bt.find_first_not_of(numbers, first);
    bname.head = bt.substr(0, first);
    if (last > -1)
    {
        bname.number = stoi(bt.substr(first, last - first));
        bname.tail = bt.substr(last);
    }
    else
    {
        bname.number = stoi(bt.substr(first));
    }

    if(aname.head < bname.head) return true;
    else if (aname.number < bname.number) return true;
    else if (aname.tail < bname.tail) return true;
    else return false;
}

vector<string> solution(vector<string> files)
{
    vector<string> answer;
    sort(files.begin(), files.end(), compare);
    for(string s: files) cout << s << endl;
    return answer;
}

int main()
{
    vector<string> test = {"foo9.txt", "foo010bar020.zip", "F-15"};
    test = solution(test);
    return 0;
}