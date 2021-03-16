#include <cstdio>

using namespace std;

int Allowance(int feel, int pay, int discomfort, int call);

int main(){
    int feel, pay, com, call;
    while(true){
        scanf("%d %d %d %d", &feel, &pay, &com, &call);
        // 0 0 0 0을 입력해 종료
        if((feel | pay | com | call) == 0) return 0;
        int result = Allowance(feel, pay, com, call);
        printf("%i\n", result);
    }
}

int Allowance(int feel=2, int pay=10, int discomfort=70, int call=5){
    if(feel == 1){
        if(call < 9) return 1000;
        else return 5000;
    } else if(feel == 3){
        if(call < 10) return 10000;
        else return 50000;
    } else{
        if(call >= 10) return 50000;
        else{
            if(discomfort >= 64) return 1000;
            else if(discomfort <= 58) return 10000;
            else{
                if(call * 15 - pay * 2 - discomfort >= 0) return 5000;
                else return 1000;
            }
        }
    }
}