package Baekjoon.Stack.P1874;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Stack;

class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        StringBuilder answer = new StringBuilder();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        int index = 1;
        for(int n=0; n<N; n++){
            int i = Integer.parseInt(br.readLine());
            for(; index <= i; index++){
                stack.push(index);
                answer.append("+\n");
            }
            if(stack.pop() != i){
                answer = new StringBuilder("NO");
                break;
            }
            answer.append("-\n");
        }

        System.out.println(answer.toString());

        br.close();
    }
}