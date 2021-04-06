package Baekjoon.Array.P1475;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String N = sc.next();
        
        int[] count = new int[10];

        for(char c: N.toCharArray()){
            count[c-'0']++;
        }
        count[6] = (int) Math.ceil((count[6] + count[9]) / 2.0);
        count[9] = 0;

        int answer = 0;
        for(int c: count){
            if(answer < c) answer = c;
        }

        System.out.println(answer);

        sc.close();
    }
}