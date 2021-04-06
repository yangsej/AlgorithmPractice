package Baekjoon.Array.P11328;

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        
        for(int n=0; n < N; n++){
            String A = sc.next(), B = sc.next();

            int[] count = new int[26];
            for(char c: A.toCharArray()){
                count[c-'a']++;
            }
            for(char c: B.toCharArray()){
                count[c-'a']--;
            }

            String answer = "Possible";
            for(int c: count){
                if(c != 0){
                    answer = "Impossible";
                    break;
                }
            }
            
            System.out.println(answer);
        }

        sc.close();
    }
}