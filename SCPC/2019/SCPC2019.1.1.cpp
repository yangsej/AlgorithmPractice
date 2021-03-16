/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <cstdio>

int Answer;
int M[1000001] = {0};

int main(int argc, char **argv)
{
    M[2] = 1;
    for (int i = 3; i < 1000000; i++)
    {
        M[i++] = M[(i + 1) / 2] + 2;
        M[i] = M[i / 2] + 1;
    }

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
        int N1, N2;
        /////////////////////////////////////////////////////////////////////////////////////////////
        /*
		   Implement your algorithm here.
		   The answer to the case will be stored in variable Answer.
		 */
        /////////////////////////////////////////////////////////////////////////////////////////////

        // Print the answer to standard output(screen).
        printf("Case #%i\n", test_case + 1);

        Answer = 0;
        scanf("%d %d", &N1, &N2);
        for (int j = N1; j <= N2; j++)
        {
            Answer += M[j];
        }
        printf("%i\n", Answer);
    }

    return 0; //Your program should return 0 on normal termination.
}