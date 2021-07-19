/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

import java.util.Scanner;
import java.util.Arrays;

/*
   As the name of the class should be Solution , using Solution.java as the filename is recommended.
   In any case, you can execute your program by running 'java Solution' command.
 */
class Solution {
	static long Answer;

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
			Answer = 0;

			int N = sc.nextInt(), M = sc.nextInt();

			int[][] S = new int[N][];
			int[][] Half = {{-1, -1}, {-1, -1}};
			int min1 = 0;
			int oddcount = 0, evencount = 0;
			for(int n=0; n<N; n++){
				int L = sc.nextInt();
				S[n] = new int[L];

				// 짝수면 최소값 4개(4 * 1)
				// 홀수면 최소값 4개(3 * 1 + 1 * 2)
				// 그룹 2개는 절반으로 최소값 2개로 줄일 수 있음
				for(int l=0; l<L; l++){
					S[n][l] = sc.nextInt();
				}
				Arrays.sort(S[n]);

				Answer += S[n][0] + S[n][1] + S[n][2] + S[n][3];
				if(L % 2 == 1){
					oddcount++;
					Answer += S[n][0];
				} else{
					evencount++;
					min1 += S[n][1];
				}

				int halfsum = S[n][2] + S[n][3];
				if(Half[0][0] == -1){
					Half[0][0] = halfsum;
					Half[0][1] = L;
				} else if(Half[1][0] == -1){
					Half[1][0] = halfsum;
					Half[1][1] = L;
				} else if(halfsum > Half[0][0]){
					Half[0][0] = halfsum;
					Half[0][1] = L;
				} else if(halfsum > Half[1][0]){
					Half[1][0] = halfsum;
					Half[1][1] = L;
				}
			}

			if(oddcount == 2 && evencount > 0){
				if(Half[0][1] % 2 == 1 && Half[1][1] % 2 == 1){
					Answer += min1;
				}
			}
			Answer -= Half[0][0] + Half[1][0];

			// Print the answer to standard output(screen).
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}