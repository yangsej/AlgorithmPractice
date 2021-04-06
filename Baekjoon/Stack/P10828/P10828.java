package Baekjoon.Stack.P10828;

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;


class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        StringBuilder answer = new StringBuilder();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        for(int n=0; n<N; n++){
            String line = br.readLine();
            StringTokenizer st = new StringTokenizer(line);
            String op = st.nextToken();
            switch(op){
                case "push":
                    stack.push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    if(stack.empty()) answer.append(-1);
                    else answer.append(stack.pop());
                    answer.append("\n");
                    break;
                case "size":
                    answer.append(stack.size());
                    answer.append("\n");
                    break;
                case "empty":
                    if(stack.empty()) answer.append(1);
                    else answer.append(0);
                    answer.append("\n");
                    break;
                case "top":
                    if(stack.empty()) answer.append(-1);
                    else answer.append(stack.peek());
                    answer.append("\n");
                    break;
            }
        }

        System.out.println(answer.toString());

        br.close();
    }
}