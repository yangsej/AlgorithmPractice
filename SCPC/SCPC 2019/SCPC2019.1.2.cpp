/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <iostream>
#include <cmath>
#define _USE_MATH_DEFINES

using namespace std;

long double Answer;

int main(int argc, char **argv)
{
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

    cin >> T;
    for (test_case = 0; test_case < T; test_case++)
    {
        int R, S, E, N;
        cin >> R >> S >> E >> N;
        long double round = M_PI * R / 2;

        Answer = E - S;
        int l[1000], r[1000], h[1000];
        for (int i = 0; i < N; i++)
        {
            cin >> l[i] >> r[i] >> h[i];
            if (l[i] > E)
                break;
            if (h[i] > 2 * R)
                Answer += h[i] + round - 2 * R;
            else
                Answer += round * h[i] / 2 / R;
            if (r[i] > E)
                break;
            if (h[i] > 2 * R)
                Answer += h[i] + round - 2 * R;
            else
                Answer += round * h[i] / 2 / R;
        }

        /////////////////////////////////////////////////////////////////////////////////////////////
        /*
		   Implement your algorithm here.
		   The answer to the case will be stored in variable Answer.
		 */
        /////////////////////////////////////////////////////////////////////////////////////////////

        // Print the answer to standard output(screen).

        cout.precision(12);
        cout << "Case #" << test_case + 1 << endl;
        cout << Answer << endl;
    }

    return 0; //Your program should return 0 on normal termination.
}