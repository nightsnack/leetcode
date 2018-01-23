package demo.algorithm;

public class LCS {
    public static void main(String[] args) {
        char x[] = {'A', 'B', 'C', 'B', 'D', 'A', 'B'};
        char y[] = {'B', 'D', 'C', 'A', 'B', 'A'};
        LcsLenth(x,y);
    }

    public static int LcsLenth(char[] x, char[] y) {
        int[][] c = new int[x.length + 1][y.length + 1];
        int[][] b = new int[x.length + 1][y.length + 1];
        for (int i = 0; i < y.length + 1; i++) {
            c[0][i] = 0;
        }
        for (int i = 0; i < x.length + 1; i++) {
            c[i][0] = 0;
        }
        for (int i = 1; i < x.length + 1; i++) {
            for (int j = 1; j < y.length + 1; j++) {
                if (x[i - 1] == y[j - 1]) {
                    c[i][j] = c[i - 1][j - 1] + 1;  //X[i] equals Y[j] LCS (x[i], y[j]) = LCS (x[i-1], y[j-1]) + 1
                    b[i][j] = 3;    //LCS = LCS[i-1][j-1] + x[i]/y[j]
                } else if (c[i - 1][j] < c[i][j - 1]) {
                    c[i][j] = c[i][j-1];
                    b[i][j] = 1;    //LCS = LCS(X[i],y[j-1)
                } else {
                    c[i][j] = c[i-1][j];
                    b[i][j] = 2;    //LCS = LCS(x[i-1],y[j])
                }

            }
        }
        printLCS(x,b,x.length,y.length);

        return c[x.length][y.length];

    }


    public static void printLCS(char[] x, int[][] b, int i, int j) {
        if (i==0 || j ==0)
            return;
        if (b[i][j] == 3) {
            printLCS(x,b,i-1,j-1);
            System.out.printf(x[i-1]+"");
        }
        else if (b[i][j] == 1) {
            printLCS(x,b,i,j-1);
        } else if (b[i][j] == 2)
            printLCS(x,b,i-1,j);
    }

}
