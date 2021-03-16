/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <cstdio>
#include <cmath>

using namespace std;

int Answer;

int main(int argc, char **argv)
{
    setbuf(stdout, NULL);
    int T, test_case;
    /*
	   The freopen function below opens input.txt file in read only mode, and afterward,
	   the program will read from input.txt file instead of standard(keyboard) input.
	   To test your program, you may save input data in input.txt file,
	   and use freopen function to read from the file when using cin function.
	   You may remove the comment symbols(//) in the below statement and use it.
	   Use #include<cstdio> or #include <stdio.h> to use the function in your program.
	   But before submission, you must remove the freopen function or rewrite comment symbols(//).
	 */

    // freopen("input.txt", "r", stdin);

    scanf("%d", &T);
    for (test_case = 0; test_case < T; test_case++)
    {
        Answer = 0;
        long long x, y;
        scanf("%d %d", &x, &y);
        for (long long i = x; i <= y; i++)
        {
            long long sum = 0, jump = 0;
            while (sum != i)
            {
                int ir = (int)sqrt((i - sum) * 2) + 1;
                long long temp = ir * (ir + 1) / 2;
                printf("%lli %lli %lli %lli \n", ir, temp, sum, jump);
                while (temp > i - sum)
                {
                    ir--;
                    temp = ir * (ir + 1) / 2;
                }
                sum += temp;
                jump += ir;
                printf("%lli %lli %lli %lli \n", ir, temp, sum, jump);
            }
            if (Answer < jump)
                Answer = jump;
        }

        /////////////////////////////////////////////////////////////////////////////////////////////
        /*
		   Implement your algorithm here.
		   The answer to the case will be stored in variable Answer.
		 */
        /////////////////////////////////////////////////////////////////////////////////////////////

        // Print the answer to standard output(screen).
        printf("Case #%i\n", test_case + 1);
        printf("%i\n", Answer);
    }

    return 0; //Your program should return 0 on normal termination.
}