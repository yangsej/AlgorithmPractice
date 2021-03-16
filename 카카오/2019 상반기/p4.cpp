#include <string>
#include <vector>

using namespace std;

int main(vector<string> words, vector<string> queries) {
    vector<int> answer(queries.size());
    for(int i=0; i<queries.size(); i++){
        for(int j=0; j<words.size(); j++){
            size_t start = queries[i].find('?'), end = queries[i].rfind('?');
            string temp = queries[i].replace(start, end, "");
            size_t pos = words[j].find(temp);
            if(start == 0){
                if(pos > end-start) answer[i]++;
            } else{
                if(queries[i].size() - pos - temp.size() > end - start) answer[i]++;
            }
        }
    }

    return 0;
}