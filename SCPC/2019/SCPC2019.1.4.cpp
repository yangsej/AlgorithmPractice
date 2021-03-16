/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

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
		int N, i;
		cin >> N;

		unsigned long long R[100];
		for (i = 0; i < N; i++)
		{
			cin >> R[i];
		}
		sort(R, R + N);

		long double Answer[100];
		Answer[0] = 0;
		i = 0;
		int j = N - 1;
		while (i != j)
		{
			Answer[j] = Answer[i] + 2 * sqrt(R[i] * R[j]);
			i++;
			Answer[i] = Answer[j] + 2 * sqrt(R[i] * R[j]);
			j--;
			// cout << Answer[i] << endl;
		}

		/////////////////////////////////////////////////////////////////////////////////////////////
		/*
		   Implement your algorithm here.
		   The answer to the case will be stored in variable Answer.
		 */
		/////////////////////////////////////////////////////////////////////////////////////////////

		// Print the answer to standard output(screen).
		cout << "Case #" << test_case + 1 << endl;
		for (i = 0; i < N; i++)
		{
			cout << Answer[i] << endl;
		}
	}

	return 0; //Your program should return 0 on normal termination.
}