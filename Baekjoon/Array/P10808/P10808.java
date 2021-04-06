package Baekjoon.Array.P10808;

import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.nextLine();

        sc.close();

        int[] count = new int[26];
        
        for(char c: S.toCharArray()){
            count[c-'a']++;
        }

        String answer = Arrays.toString(count).replaceAll("[^0-9 ]","");
        System.out.println(answer);
    }
}