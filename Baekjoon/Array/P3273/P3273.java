package Baekjoon.Array.P3273;

import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        
        int[] arr = new int[N];
        for(int n=0; n<N; n++){
            arr[n] = sc.nextInt();
        }
        Arrays.sort(arr);

        int X = sc.nextInt();

        int i = 0, j = N-1, answer = 0;
        while(i < j){
            int temp = arr[i] + arr[j];
            if(X < temp){
                j--;
            } else if (X > temp){
                i++;
            } else{
                answer++;
                if(arr[i+1] - arr[i] <= arr[j] - arr[j-1]) i++;
                else j--;
            }
        }

        System.out.println(answer);

        sc.close();
    }
}