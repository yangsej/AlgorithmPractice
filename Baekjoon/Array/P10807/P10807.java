package Baekjoon.Array.P10807;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i<N; i++){
            arr[i] = sc.nextInt();
        }
        int V = sc.nextInt();

        sc.close();
        
        int answer = 0;
        for(int a: arr){
            if(V == a) answer++;
        }

        System.out.println(answer);
    }
}