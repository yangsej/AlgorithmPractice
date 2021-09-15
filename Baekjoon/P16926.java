import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Locale;

public class P16926 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String input = reader.readLine();

        input.toLowerCase(Locale.ROOT);



        int[] info = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
        int N = info[0], M = info[1], R = info[2];

        int[][] arr = new int[N][];
        for(int n = 0; n < N; n++){
            input = reader.readLine();
            arr[n] = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        reader.close();


//        int answer = ;

//        System.out.println(answer);
    }
}
