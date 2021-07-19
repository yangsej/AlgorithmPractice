/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

import java.util.Scanner;

/*
   As the name of the class should be Solution , using Solution.java as the filename is recommended.
   In any case, you can execute your program by running 'java Solution' command.
 */
class Solution {
	static char[] Answer;

	public static void main(String args[]) throws Exception	{
		/*
		   The method below means that the program will read from input.txt, instead of standard(keyboard) input.
		   To test your program, you may save input data in input.txt file,
		   and call below method to read from the file when using nextInt() method.
		   You may remove the comment symbols(//) in the below statement and use it.
		   But before submission, you must remove the freopen function or rewrite comment symbols(//).
		 */		

		/*
		   Make new scanner from standard input System.in, and read data.
		 */
		Scanner sc = new Scanner(System.in);
		//Scanner sc = new Scanner(new FileInputStream("input.txt"));

		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
			int N = sc.nextInt(), M = sc.nextInt(), K = sc.nextInt();

			Answer = new char[K];

			int[][] Dirs = new int[N+1][N+1]; 
			
			for(int n=1; n<=N; n++){
				Dirs[n][0] = n;
			}

			for(int m=0; m<M; m++){
				int s = sc.nextInt(), e = sc.nextInt();
				Dirs[s][e] = 1;
			}

			for(int k=0; k<K; k++){
				int s = sc.nextInt(), e = sc.nextInt();
				Answer[k] = '0';
			}


			// Print the answer to standard output(screen).
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}