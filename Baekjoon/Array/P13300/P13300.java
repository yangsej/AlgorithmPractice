package Baekjoon.Array.P13300;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        double K = sc.nextDouble();
        
        int[][] count = new int[2][6];
        for(int n=0; n < N; n++){
            int S = sc.nextInt(), Y = sc.nextInt();

            count[S][Y-1]++;
        }

        int answer = 0;
        for(int i=0; i<2; i++){
            for(int j=0; j<6; j++){
                answer += Math.ceil(count[i][j] / K);
            }
        }

        System.out.println(answer);

        sc.close();
    }
}