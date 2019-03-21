package test.tencent;

    import java.util.Scanner;

    public class Main1 {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int k = sc.nextInt();
            int a = sc.nextInt();
            int x = sc.nextInt();
            int b = sc.nextInt();
            int y = sc.nextInt();

            long total = 0;
            long p = 1,v = 1;
            for (int i = 0; i <= x; i++) {
                a:for (int j = y; j >= 0; j--) {
                    if (a*i+b*j == k) {
                        if (i!=0 && x!=i)   {
                            p =  combination (x,i);
                        }
                            else p = 1;
                        if (j!=0 && y!=j)   {
                            v =  combination (y,j);
                        }
                        else v = 1;
                        total += p*v;
                        break a;
                    }
                }
            }

            System.out.println(total%1000000007);
        }

        /**
         * 计算阶乘数，即n! = n * (n-1) * ... * 2 * 1
         * @param n
         * @return
         */
        private static long factorial(int n) {
            return (n > 1) ? n * factorial(n - 1) : 1;
        }

        /**
         * 计算排列数，即A(n, m) = n!/(n-m)!
         * @param n
         * @param m
         * @return
         */
        public static long arrangement(int n, int m) {
            return (n >= m) ? factorial(n) / factorial(n - m) : 0;
        }

        /**
         * 计算组合数，即C(n, m) = n!/((n-m)! * m!)
         * @param n
         * @param m
         * @return
         */
        public static long combination(int n, int m) {
            try {
                return (n >= m) ? factorial(n) / factorial(n - m) / factorial(m) : 0;
            }
            catch (Exception e) {
                return n;
            }

        }
    }
