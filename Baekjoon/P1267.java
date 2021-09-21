import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1267 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());

        tokenizer = new StringTokenizer(reader.readLine());
        int Y = 0, M = 0;
        for(int n=0; n < N; n++){
            int time = Integer.parseInt(tokenizer.nextToken());

            Y += 10 * (Math.floor(time / 30) + 1);
            M += 15 * (Math.floor(time / 60) + 1);
        }

        reader.close();

        if(Y < M){
            System.out.println("Y " + Y);
        } else if(Y > M){
            System.out.println("M " + M);
        } else{
            System.out.println("Y M " + Y);
        }

    }
}
