import java.util.*;
import java.io.*;

public class Main {
    static int H, W;
    static int[][] A, B;
    static boolean[][] hasDust;
    static boolean[][][] visited;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        A = new int[H][W];
        B = new int[H][W];
        hasDust = new boolean[H][W];
        visited = new boolean[H][W][4];

        for (int i = 0; i < H; i++) {
            String line = br.readLine();
            for (int j = 0; j < W; j++) {
                A[i][j] = line.charAt(j) - '0';
                hasDust[i][j] = true;
            }
        }

        for (int i = 0; i < H; i++) {
            String line = br.readLine();
            for (int j = 0; j < W; j++) {
                B[i][j] = line.charAt(j) - '0';
            }
        }

        long totalMoves = 0;
        long lastCleanMove = 0;

        while (true) {
            if (hasDust[r][c]) {

                hasDust[r][c] = false;
                d = (d + A[r][c]) % 4;


                clearVisited();

                totalMoves++;
                lastCleanMove = totalMoves;
            } else {

                if (visited[r][c][d]) break;

                visited[r][c][d] = true;
                d = (d + B[r][c]) % 4;
                totalMoves++;
            }


            r += dr[d];
            c += dc[d];


            if (r < 0 || r >= H || c < 0 || c >= W) break;
        }


        System.out.println(lastCleanMove);
    }

    static void clearVisited() {
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                Arrays.fill(visited[i][j], false);
            }
        }
    }
}