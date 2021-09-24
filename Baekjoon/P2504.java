import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

public class P2504 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        int answer = 0;

        Stack<Character> stack = new Stack<Character>();
        Stack<Integer> nums = new Stack<Integer>();
        Stack<Integer> depths = new Stack<Integer>();
        nums.add(0);
        depths.add(0);
        for(char c : str.toCharArray()){
            int num = 0, depth = 0;

            if (c == '(' || c == '[') {
                stack.add(c);
            } else if (c == ')') {
                if(stack.isEmpty() || stack.peek() != '('){
                    answer = -1;
                    break;
                } else{
                    num = 2;
                }
            } else if (c == ']') {
                if(stack.isEmpty() || stack.peek() != '['){
                    answer = -1;
                    break;
                } else{
                    num = 3;
                }
            }

            if(num > 0){
                if(stack.isEmpty()){
                    answer = -1;
                    break;
                }

                stack.pop();

                depth = stack.size();

                if(depths.peek() < depth){
                    nums.add(num);
                    depths.add(depth);
                } else{
                    while(!depths.isEmpty() && depths.peek() >= depth){
                        if(depths.peek() == 0 || depths.peek() <= depth){
                            num += nums.pop();
                        } else{
                            num *= nums.pop();
                        }
                        depths.pop();
                    }
                    nums.add(num);
                    depths.add(depth);
                }
            }
        }

        sc.close();

        if(answer == -1 || !stack.isEmpty()){
            answer = 0;
        } else{
            answer = nums.pop();
        }

        System.out.println(answer);
    }
}
