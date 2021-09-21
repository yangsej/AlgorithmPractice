import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class P10093 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        long A = Long.parseLong(tokenizer.nextToken()), B = Long.parseLong(tokenizer.nextToken());

        reader.close();

        if(A > B){
            long temp = A;
            A = B;
            B = temp;
        }

        int length = 0;
        if(A != B){
            length = (int) (B - A - 1);
        }
        System.out.println(length); // 같은 수면 0

        long[] nums = new long[length];
        for(int i=0; i < length; i++){
            nums[i] = A + i + 1;
        }

        String answer = Arrays.stream(nums).mapToObj(String::valueOf).collect(Collectors.joining(" "));

        System.out.println(answer);
    }
}
