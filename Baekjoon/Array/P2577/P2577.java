package Baekjoon.Array.P2577;

import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt(), B = sc.nextInt(), C = sc.nextInt();

        sc.close();

        String s = Integer.toString(A * B * C);
        int[] count = new int[10];
        for(char c: s.toCharArray()){
            count[c-'0']++;
        }

        String answer = Arrays.toString(count).replaceAll("[^0-9 ]","").replaceAll(" ", "\n");
        System.out.println(answer);
    }
}