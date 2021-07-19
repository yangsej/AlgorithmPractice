package 이진수;
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
	static String Answer;

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
            int n = sc.nextInt();
            int t = sc.nextInt();

			char[] B = sc.next().toCharArray();
			char[] A = new char[n];

			for(int i=0; i<n; i++){
				A[i] = '?';
			}

			for(int i=0; i<n; i++){
				if(B[i] == '0'){
					if(i-t >= 0){
						A[i-t] = '0';
					}
					if(i+t < n){
						A[i+t] = '0';
					}
				}
			}

			for(int i=0; i<t && 0<=i-t && i+t<n; i++){
				A[i+t] = B[i];
			}

			for(int i=n-t; i<n && 0<=i-t && i+t<n; i++){
				A[i-t] = B[i];
			}

			for(int i=t; i<t*2 && 0<=i-t && i+t<n; i++){
				if(B[i] == '1'){
					if(A[i+t] == '0'){
						A[i-t] = '1';
					}
					else if(A[i+t] == '1'){
						A[i-t] = '0';
					}
					else{
						if(i+t*2 < n){
							if(B[i+t*2] == '1'){
								A[i+t] = '1';
								A[i-t] = '0';
							}
							else{
								A[i+t] = '0';
								A[i-t] = '1';
							}
						}
					}
				}
			}

			for(int i=t*2; i<n-t*2 && 0<=i-t && i+t<n; i++){
				if(B[i] == '1'){
					if(A[i-t] == '0'){
						A[i+t] = '1';
					}
					else if(A[i-t] == '1'){
						A[i+t] = '0';
					}
					else if(A[i+t] == '0'){
						A[i-t] = '1';
					}
					else if(A[i+t] == '1'){
						A[i+t] = '0';
					}
					else{
						if(B[i+t*2] == '1'){
							A[i+t] = '1';
							A[i-t] = '0';
						}
						else{
							A[i+t] = '0';
							A[i-t] = '1';
						}
					}
				}
			}
			
			for(int i=n-t*2; i<n-t && 0<=i-t && i+t<n; i++){
				if(B[i] == '1'){
					if(A[i-t] == '0'){
						A[i+t] = '1';
					}
					else if(A[i-t] == '1'){
						A[i+t] = '0';
					}
					else if(A[i+t] == '0'){
						A[i-t] = '1';
					}
					else if(A[i+t] == '1'){
						A[i+t] = '0';
					}
					else{
						if(i-t*2 >= 0){
							if(B[i-t*2] == '1'){
								A[i+t] = '0';
								A[i-t] = '1';
							}
							else{
								A[i+t] = '1';
								A[i-t] = '0';
							}
						}
					}
				}
			}

			Answer = String.valueOf(A);

			// Print the answer to standard output(screen).
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}