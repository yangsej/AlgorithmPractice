#include <string>
#include <vector>

using namespace std;

string solution(string p) {
    /* 1번 */
    if(p == "") return p;
    
    /* 2번 */
    int start = 0, count = 0, length = p.length();
    string u, v = p;
    for(int i=0; i<length; i++){
        if(v[i] == '(') count++;
        else count--;
        
        if(count == 0){
            u = v.substr(start, i-start+1);
            start = i+1;
            v = v.substr(start);
        }
    }

    
    
    string answer = "";
    
    return answer;
}