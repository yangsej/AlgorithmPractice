import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P2752 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        int[] nums = {0, 0, 0};
        for(int i=0; i<3; i++){
            nums[i] = Integer.parseInt(tokenizer.nextToken());
        }

        reader.close();

        Arrays.sort(nums);

        String answer = "";
        for(int i=0; i<3; i++){
            answer += nums[i] + " ";
        }

        System.out.print(answer);
    }
}
