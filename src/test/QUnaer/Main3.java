package test.QUnaer;

public class Main3 {
}
//
//#include<cstdio>
//#include<cstring>
//#include<algorithm>
//#define Max 100010
//        #define LL long long
//
//        using namespace std;
//
//        struct A
//        {
//        int x;
//        int y;
//        }t[Max], m[Max];
//
//        int mark[Max];
//
//        bool cmp(A a, A b)
//        {
//        if(a.x != b.x)return a.x > b.x;
//        return a.y > b.y;
//        }
//
//        int main()
//        {
//        int N, M;
//        while(scanf("%d %d", &N, &M) != EOF)
//        {
//        for(int i = 0; i < N; i++)
//        scanf("%d %d", &m[i].x, &m[i].y);
//        for(int j = 0; j < M; j++)
//        scanf("%d %d", &t[j].x, &t[j].y);
//        sort(t, t + M, cmp);
//        sort(m, m + N, cmp);
//
//        /*for(int i = 0; i < N; i++)
//            printf("%d %d\n", t[i].x, t[i].y);*/
//
//        LL sum = 0;
//        int count = 0;
//        memset(mark, 0, sizeof(mark));
//        int j = 0;
//        for(int i = 0; i < M; i++)
//        {
//        while(j < N && m[j].x >= t[i].x)
//        {
//        mark[m[j].y]++;
//        j++;
//        }
//        for(int k = t[i].y; k <= 100; k++)
//        {
//        if(mark[k])
//        {
//        mark[k]--;
//        count++;
//        sum += (LL)(200 * t[i].x + 3 * t[i].y);
//        //printf("sum = %lld\n", sum);
//        break;
//        }
//        }
//        }
//        printf("%d %lld\n", count, sum);
//        }
//        return 0;
//        }