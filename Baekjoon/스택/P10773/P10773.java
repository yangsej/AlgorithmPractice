package Baekjoon.Stack.P10773;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Stack;


class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int K = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        for(int k=0; k<K; k++){
            int i = Integer.parseInt(br.readLine());
            
            if(i == 0) stack.pop();
            else stack.push(i);
        }

        int answer = 0;
        for(int s: stack) answer += s;

        System.out.println(answer);

        br.close();
    }
}