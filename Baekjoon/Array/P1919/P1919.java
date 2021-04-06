package Baekjoon.Array.P1919;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String A = sc.next();
        String B = sc.next();
        
        int[] count = new int[26];

        for(char c: A.toCharArray()){
            count[c-'a']++;
        }
        for(char c: B.toCharArray()){
            count[c-'a']--;
        }

        int answer = 0;
        for(int c: count){
            answer += Math.abs(c);
        }

        System.out.println(answer);

        sc.close();
    }
}